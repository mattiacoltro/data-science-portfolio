## Test-set metrics

| Model | f1_macro | f1_micro | roc_auc_macro | pr_auc_macro | hamming_loss | subset_accuracy |
|---|---|---|---|---|---|---|
| Final model: BiGRU, tuned thresholds | 0.6810 | 0.7723 | 0.9879 | 0.7139 | 0.0163 | 0.9242 |
| Baseline: TF-IDF + LR, threshold 0.5 | 0.5656 | 0.6808 | 0.9814 | 0.6499 | 0.0295 | 0.8799 |
| Baseline: TF-IDF + LR, tuned thresholds | 0.6264 | 0.7291 | 0.9814 | 0.6499 | 0.0205 | 0.9079 |

## Final model, per label

| label | precision | recall | f1 | roc_auc | pr_auc |
|---|---|---|---|---|---|
| toxic | 0.8750 | 0.7537 | 0.8098 | 0.9814 | 0.8975 |
| severe_toxic | 0.4478 | 0.6820 | 0.5406 | 0.9908 | 0.4817 |
| obscene | 0.8508 | 0.8186 | 0.8344 | 0.9892 | 0.9084 |
| threat | 0.5753 | 0.5833 | 0.5793 | 0.9952 | 0.5801 |
| insult | 0.7707 | 0.7316 | 0.7507 | 0.9858 | 0.8215 |
| identity_hate | 0.5074 | 0.6540 | 0.5714 | 0.9853 | 0.5942 |
