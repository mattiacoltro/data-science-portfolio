"""Evaluate the final anti-hater model (regularised BiGRU) on the held-out test set.

Reproduces the numbers reported in the README without retraining anything:
  1. downloads the public dataset and recreates the same stratified train/val/test split (seed 42)
  2. rebuilds the preprocessing (same cleaning rules + the vocabulary saved by the notebook)
  3. loads the saved weights of the final model and predicts the test set
  4. refits the TF-IDF + Logistic Regression baseline (a few minutes) and evaluates it on the same test set,
     both with the default 0.5 threshold and with per-label thresholds tuned on the validation set
  5. writes results/test_metrics.json, results/test_metrics_per_label.csv, results/test_metrics.md
     and results/confusion_matrices_test.png

Run from the anti-hater-filter folder:   python evaluate_final_model.py
Options:  --skip-baseline   evaluate only the final model
          --refit-vocab     rebuild the vocabulary from the training split instead of loading the saved one
"""
import argparse
import html
import json
import re
import time
import unicodedata
import pickle
from pathlib import Path

import contractions
import emoji
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from iterstrat.ml_stratifiers import MultilabelStratifiedShuffleSplit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, average_precision_score, confusion_matrix, f1_score,
                             hamming_loss, precision_recall_fscore_support, roc_auc_score)
from sklearn.multioutput import MultiOutputClassifier

# ----------------------------------------------------------------------------- configuration
DATA_URL = "https://proai-datasets.s3.eu-west-3.amazonaws.com/Filter_Toxic_Comments_dataset.csv"
LABEL_NAMES = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
SEED, MAX_LEN, VOCAB_SIZE, EMBEDDING_DIM = 42, 200, 20000, 300
# per-label thresholds chosen on the validation set (notebook, section "Threshold Optimization")
THRESHOLDS = np.array([0.5, 0.25, 0.5, 0.3, 0.5, 0.15])
WEIGHTS_PATH = Path("models/model_10_BiGRU_Reg_weights.h5")
VOCAB_PATH = Path("hate_speech_vocabulary.pkl")
RESULTS_DIR = Path("results")
# values printed by the notebook for the same model on the same test set (consistency check)
EXPECTED_TEST_SIZE = 23936
EXPECTED_F1_MACRO = 0.6810436527072818


# ----------------------------------------------------------------------------- text cleaning (same rules as the notebook)
def clean_text(text):
    text = unicodedata.normalize("NFKD", text)
    text = html.unescape(text)
    text = re.sub(r"[\u200b\u200d\ufeff\u00ad]", "", text)
    text = re.sub(r"http\S+|www\.\S+", "<URL>", text)
    text = re.sub(r"@\w+", "<USER>", text)
    text = re.sub(r"#(\w+)", r"<HASHTAG> \1", text)
    text = re.sub(r"\S+@\S+", "<EMAIL>", text)
    text = contractions.fix(text)
    text = emoji.demojize(str(text), delimiters=("<EMOJI_", ">"))
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    text = re.sub(r"([!?.,;:]){3,}", r"\1\1", text)
    text = re.sub(r"([.,!?();:])", r" \1 ", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower().strip()


def clean_all(texts, name):
    start = time.time()
    out = [clean_text(t) for t in texts]
    print(f"  cleaned {len(out):,} {name} texts in {time.time() - start:.0f}s")
    return out


# ----------------------------------------------------------------------------- data
def load_splits():
    dataset = pd.read_csv(DATA_URL)
    texts = dataset["comment_text"].values
    labels = dataset[LABEL_NAMES].values
    train_idx, temp_idx = next(MultilabelStratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=SEED).split(texts, labels))  # type: ignore[arg-type]
    x_temp, y_temp = texts[temp_idx], labels[temp_idx]
    val_idx, test_idx = next(MultilabelStratifiedShuffleSplit(n_splits=1, test_size=0.5, random_state=SEED).split(x_temp, y_temp))
    return (texts[train_idx], labels[train_idx]), (x_temp[val_idx], y_temp[val_idx]), (x_temp[test_idx], y_temp[test_idx])


# ----------------------------------------------------------------------------- final model
def build_vectorizer(vocabulary=None, cleaned_train=None):
    from keras.layers import TextVectorization

    vec = TextVectorization(max_tokens=VOCAB_SIZE, output_mode="int", output_sequence_length=MAX_LEN, standardize=None)
    if vocabulary is not None:
        vec.set_vocabulary(vocabulary)
        if vec.get_vocabulary() != list(vocabulary):
            raise SystemExit("The saved vocabulary was not restored identically. Re-run with --refit-vocab.")
    else:
        vec.adapt(cleaned_train)
    return vec


def build_bigru(embedding_rows):
    """Same architecture as build_gru(config=...) in the notebook (final model: BiGRU, regularised).
    embedding_rows = len(vocabulary) + 1: load_embeddings() in the notebook adds one row for padding."""
    from keras.layers import GRU, Bidirectional, Dense, Dropout, Embedding, Input
    from keras.models import Model

    inp = Input(shape=(MAX_LEN,), dtype="int32", name="text_input")
    x = Embedding(input_dim=embedding_rows, output_dim=EMBEDDING_DIM, weights=[np.zeros((embedding_rows, EMBEDDING_DIM), "float32")],
                  trainable=False, mask_zero=True, name="embedding")(inp)
    x = Dropout(0.2)(x)
    x = Bidirectional(GRU(units=64, dropout=0.2, recurrent_dropout=0.0, name="gru"), name="bidirectional_gru")(x)
    x = Dropout(0.3)(x)
    out = Dense(6, activation="sigmoid", name="output")(x)
    return Model(inputs=inp, outputs=out, name="GRU")


def predict_final_model(cleaned_test, vocabulary, cleaned_train):
    vec = build_vectorizer(vocabulary, cleaned_train)
    sequences = vec(np.array(cleaned_test)).numpy()
    model = build_bigru(len(vec.get_vocabulary()) + 1)
    model.load_weights(str(WEIGHTS_PATH))
    if not np.abs(model.get_layer("embedding").get_weights()[0]).sum() > 0:
        raise SystemExit("The weights file does not contain the embedding matrix: it must be rebuilt from FastText (see README).")
    return model.predict(sequences, batch_size=512, verbose=0)


# ----------------------------------------------------------------------------- baseline
def fit_baseline(cleaned_train, y_train, cleaned_val, cleaned_test):
    vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1, 2), min_df=2, max_df=0.95, sublinear_tf=True,
                                 strip_accents="unicode", analyzer="word", token_pattern=r"\w+", lowercase=True)
    x_train = vectorizer.fit_transform(cleaned_train)
    clf = MultiOutputClassifier(LogisticRegression(max_iter=1000, C=1.0, solver="lbfgs", class_weight="balanced",
                                                   random_state=SEED), n_jobs=-1).fit(x_train, y_train)

    def proba(texts):
        return np.column_stack([p[:, 1] for p in clf.predict_proba(vectorizer.transform(texts))])

    return proba(cleaned_val), proba(cleaned_test)


def tune_thresholds(y_true, y_proba):
    """Per-label threshold maximising F1 on the validation set (same grid as the notebook)."""
    grid = np.arange(0.05, 0.95, 0.05)
    return np.array([max(grid, key=lambda t: f1_score(y_true[:, i], (y_proba[:, i] > t).astype(int), zero_division=0))
                     for i in range(y_true.shape[1])])


# ----------------------------------------------------------------------------- metrics
def global_metrics(y_true, y_pred, y_proba):
    return {"f1_macro": f1_score(y_true, y_pred, average="macro", zero_division=0),
            "f1_micro": f1_score(y_true, y_pred, average="micro", zero_division=0),
            "roc_auc_macro": roc_auc_score(y_true, y_proba, average="macro"),
            "pr_auc_macro": average_precision_score(y_true, y_proba, average="macro"),
            "hamming_loss": hamming_loss(y_true, y_pred),
            "subset_accuracy": accuracy_score(y_true, y_pred)}


def per_label_metrics(y_true, y_pred, y_proba):
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average=None, zero_division=0)
    return pd.DataFrame({"label": LABEL_NAMES, "precision": precision, "recall": recall, "f1": f1,
                         "roc_auc": [roc_auc_score(y_true[:, i], y_proba[:, i]) for i in range(6)],
                         "pr_auc": [average_precision_score(y_true[:, i], y_proba[:, i]) for i in range(6)]})


def plot_confusion_matrices(y_true, y_pred, path):
    fig, axes = plt.subplots(2, 3, figsize=(10, 6))
    for i, ax in enumerate(axes.flatten()):
        cm = confusion_matrix(y_true[:, i], y_pred[:, i])  # y_true is the TEST label vector of that label
        ax.imshow(cm, cmap="Blues")
        for (r, c), v in np.ndenumerate(cm):
            ax.text(c, r, f"{v:,}", ha="center", va="center", fontsize=8,
                    color="white" if v > cm.max() / 2 else "black")
        ax.set_title(LABEL_NAMES[i], fontsize=9, fontweight="bold")
        ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
        ax.set_xlabel("Predicted", fontsize=8); ax.set_ylabel("True", fontsize=8)
    fig.suptitle("Confusion matrices on the test set (final model, tuned thresholds)", fontsize=10, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(path, dpi=200)
    plt.close(fig)


def to_markdown(df):
    cols = list(df.columns)
    lines = ["| " + " | ".join(map(str, cols)) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(f"{v:.4f}" if isinstance(v, float) else str(v) for v in row) + " |")
    return "\n".join(lines)


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skip-baseline", action="store_true")
    ap.add_argument("--refit-vocab", action="store_true")
    args = ap.parse_args()
    for p in (WEIGHTS_PATH,) + (() if args.refit_vocab else (VOCAB_PATH,)):
        if not p.exists():
            raise SystemExit(f"Missing file: {p}. Run this script from the anti-hater-filter folder.")
    RESULTS_DIR.mkdir(exist_ok=True)

    print("1/4 Loading data and recreating the stratified split...")
    (x_train, y_train), (x_val, y_val), (x_test, y_test) = load_splits()
    print(f"  train={len(x_train):,}  val={len(x_val):,}  test={len(x_test):,}")
    if len(x_test) != EXPECTED_TEST_SIZE:
        print(f"  WARNING: the test set has {len(x_test)} rows, the notebook had {EXPECTED_TEST_SIZE}: "
              "different package versions or a changed dataset.")

    print("2/4 Cleaning texts...")
    need_train = args.refit_vocab or not args.skip_baseline
    cleaned_train = clean_all(x_train, "train") if need_train else None
    cleaned_val = clean_all(x_val, "validation") if not args.skip_baseline else None
    cleaned_test = clean_all(x_test, "test")

    print("3/4 Final model (BiGRU) on the test set...")
    vocabulary = None if args.refit_vocab else pickle.load(open(VOCAB_PATH, "rb"))
    proba_final = predict_final_model(cleaned_test, vocabulary, cleaned_train)
    pred_final = (proba_final > THRESHOLDS).astype(int)

    rows = {"Final model: BiGRU, tuned thresholds": (pred_final, proba_final)}
    thresholds_used = {"Final model: BiGRU, tuned thresholds": THRESHOLDS.tolist()}
    if not args.skip_baseline:
        print("4/4 Baseline TF-IDF + Logistic Regression (a few minutes)...")
        proba_val_base, proba_test_base = fit_baseline(cleaned_train, y_train, cleaned_val, cleaned_test)
        rows["Baseline: TF-IDF + LR, threshold 0.5"] = ((proba_test_base > 0.5).astype(int), proba_test_base)
        thr_base = tune_thresholds(y_val, proba_val_base)
        rows["Baseline: TF-IDF + LR, tuned thresholds"] = ((proba_test_base > thr_base).astype(int), proba_test_base)
        thresholds_used["Baseline: TF-IDF + LR, threshold 0.5"] = [0.5] * 6
        thresholds_used["Baseline: TF-IDF + LR, tuned thresholds"] = thr_base.tolist()

    summary = {name: global_metrics(y_test, pred, proba) for name, (pred, proba) in rows.items()}
    per_label = pd.concat([per_label_metrics(y_test, pred, proba).assign(model=name)
                           for name, (pred, proba) in rows.items()])
    table = pd.DataFrame(summary).T
    print("\nGlobal metrics on the test set:\n" + table.round(4).to_string())
    print("\nFinal model, per label:\n" + per_label[per_label["model"].str.startswith("Final")].round(4).to_string(index=False))

    got = summary["Final model: BiGRU, tuned thresholds"]["f1_macro"]
    status = "OK" if abs(got - EXPECTED_F1_MACRO) < 0.005 else "MISMATCH"
    print(f"\nConsistency check vs the notebook (macro-F1 {EXPECTED_F1_MACRO:.4f}): got {got:.4f} -> {status}")

    out = {"test_size": int(len(x_test)), "positives_per_label": dict(zip(LABEL_NAMES, y_test.sum(axis=0).astype(int).tolist())),
           "thresholds": thresholds_used, "global": summary,
           "per_label": {n: g.drop(columns="model").set_index("label").to_dict("index") for n, g in per_label.groupby("model")},
           "consistency_check": {"expected_f1_macro": EXPECTED_F1_MACRO, "got": got, "status": status}}
    (RESULTS_DIR / "test_metrics.json").write_text(json.dumps(out, indent=2, default=float), encoding="utf-8")
    per_label.to_csv(RESULTS_DIR / "test_metrics_per_label.csv", index=False)
    md = ["## Test-set metrics", "", to_markdown(table.rename_axis("Model").reset_index()), "",
          "## Final model, per label", "",
          to_markdown(per_label[per_label["model"].str.startswith("Final")].drop(columns="model"))]
    (RESULTS_DIR / "test_metrics.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    plot_confusion_matrices(y_test, pred_final, RESULTS_DIR / "confusion_matrices_test.png")
    print(f"\nWritten in {RESULTS_DIR}/: test_metrics.json, test_metrics_per_label.csv, test_metrics.md, confusion_matrices_test.png")


if __name__ == "__main__":
    main()
