# Credit Scoring Prediction

Binary classification of credit card applicants (`TARGET`: 1 = reliable, 0 = unreliable)
on 338,426 applicants, with interpretable explanations of the predictions.
The original assignment is kept at the bottom of this page.

## Tech stack

- **Language**: Python
- **Data handling**: pandas, NumPy, SciPy (statistical tests)
- **Visualisation**: Matplotlib, seaborn
- **Modelling**: scikit-learn (pipelines, preprocessing, Logistic Regression, KNN,
  Decision Tree, Random Forest, Naive Bayes), XGBoost, LightGBM
- **Class imbalance**: imbalanced-learn (SMOTE, random over/undersampling),
  class weights
- **Feature selection**: mutual information, tree-based feature importance
- **Explainability**: SHAP (summary and waterfall plots)
- **Environment**: Jupyter notebook (ipykernel), pinned dependencies in `requirements.txt`

## Results

Final model: **LightGBM, base configuration** (no resampling, no class weights, no
feature selection), evaluated once on a stratified hold-out test set
(20%, 67,686 applicants, 5,944 of them reliable, `random_state=42`).

| Metric (class 1 = reliable) | Value |
|---|---|
| Precision | 0.688 |
| Recall | 0.933 |
| F1 | 0.792 |
| Accuracy | 0.957 |
| ROC-AUC | 0.979 |

Baseline comparison on the same test set (no resampling, no tuning):

| Model | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|
| **LightGBM** | 0.688 | 0.933 | 0.792 | 0.979 |
| XGBoost | 0.688 | 0.917 | 0.787 | 0.978 |
| Decision Tree | 0.688 | 0.922 | 0.788 | 0.976 |
| Random Forest | 0.687 | 0.167 | 0.268 | 0.977 |
| KNN (k=3) | 0.677 | 0.734 | 0.704 | 0.954 |
| Logistic Regression | 0.520 | 0.208 | 0.298 | 0.918 |
| Gaussian Naive Bayes | 0.115 | 0.970 | 0.205 | 0.821 |

Precision on class 1 is the main metric: a false positive is an unreliable applicant
who gets a card. At the default threshold, about 31% of the applicants the model
approves are unreliable.

## Approach

1. **EDA and cleaning**: one incomplete record removed, constant column `FLAG_MOBIL`
   dropped, missing `OCCUPATION_TYPE` kept as its own category with a flag,
   `DAYS_EMPLOYED` anomalies (positive values) flagged and imputed with the median,
   outliers kept because they are plausible values.
2. **Evaluation protocol**: stratified 80/20 hold-out split (target imbalance about
   1:10), chosen over cross-validation for computational cost.
3. **Baselines**: seven model families with preprocessing adapted to each one.
4. **Imbalance handling**: random oversampling, random undersampling and SMOTE with
   ratios from 0.2 to 1.0 (applied inside the pipeline, so only on training data),
   and class weights. According to the notebook, none improved precision, F1 or
   ROC-AUC meaningfully over the base models; only recall increased, at a high
   computational cost.
5. **Feature selection**: mutual information and feature importance (XGBoost,
   LightGBM); the selected subset did not give meaningful gains.
6. **Model choice**: LightGBM base, the simplest option with the best overall metrics.
7. **Explainability**: SHAP summary plot and a waterfall plot. Income, age and
   employment length are the features that contribute the most.

Dataset check: all 338,426 applicants have a distinct feature profile (no duplicates),
so no profile is shared between train and test.

## Repository content

- `credit_scoring_project.ipynb`: full analysis, with outputs saved.
- `requirements.txt`: pinned versions used for the results.

## How to run

```bash
python -m venv venv
venv\Scripts\activate        # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

Open the notebook and run all cells. The dataset is downloaded from a public URL.
The full run is slow (the logged model fits add up to about 53 minutes).

## Limitations

- **The dataset is likely synthetic or heavily preprocessed.** Several signals point
  in that direction: (i) very high discrimination (ROC-AUC 0.98 for the final model)
  despite weak pairwise correlations between features and target; (ii) no duplicate
  profiles among the 338,426 applicants; (iii) a clean dataset with a single
  incomplete record; (iv) a class definition that is the reverse of real credit
  portfolios: here the reliable applicants (`TARGET = 1`) are only 8.8% of the data,
  while in real credit data defaults are the rare class.
- **Single hold-out test set used also for model selection.** Models, resampling
  ratios and feature subsets were compared on the same test set that reports the final
  metrics, with no separate validation set or cross-validation. The reported figures
  are likely optimistic, even if the differences between configurations are small.
- **Fixed decision threshold.** Metrics are computed at the default 0.5 threshold,
  with no precision-recall curve or cost analysis, although precision is the stated
  priority. A threshold tuned on separate data could raise precision at the expense of
  recall.
- **Explainability is illustrative.** The waterfall plot explains a hand-built
  applicant, not a real rejected one.
- **Protected attributes.** Gender (`CODE_GENDER`) and age (`DAYS_BIRTH`) are model
  features; no fairness analysis has been done. This would need to be addressed in a
  real credit setting.

---

<details>
<summary>Original assignment</summary>

# Prediction of creditworthiness
You have been hired by Pro National Bank as a data scientist, and your first task is to create a model that can estimate the creditworthiness of customers, in order to help the dedicated team understand whether or not to accept credit card applications.



## Data description

You are given anonymized data from customers who have already obtained credit cards and are regularly pay their installments. The data are available in a CSV ﬁle [credit_scoring.csv](https://proai-datasets.s3.eu-west-3.amazonaws.com/credit_scoring.csv) that contains the information of account holders who have applied for a line of credit.

- ID: customer identiﬁcation number
- CODE_GENDER: gender of the client
- FLAGOWNCAR: indicator of car ownership
- FLAGOWNREALTY: indicator of a house ownership 
- CNT_CHILDREN: number of children
- AMTINCOMETOTAL: total annual income
- NAMEINCOMETYPE: income type
- NAMEEDUCATIONTYPE: education level
- NAMEFAMILYSTATUS: civil status
- NAMEHOUSINGTYPE: housing type
- DAYS_BIRTH: number of days elapsed since birth
- DAYS_EMPLOYED: number of days since date of employment (if positive, indicate the number of days since unemployed)
- FLAG_MOBIL: indicator of the existence of a mobile phone number
- FLAGWORKPHONE: indicator of the existence of a job phone number
- FLAG_PHONE: indicator of the existence of a phone number
- FLAG_EMAIL: indicator of the existence of a e-mail
- OCCUPATION_TYPE: occupation type
- CNTFAMMEMBERS: number of family members
- TARGET: variable that is 1 if the customer has high creditworthness (constant payment of installments), 0 otherwise.

## Goal

You have to make a model that predicts the given target, which is the TARGET variable that indicates whether the
customer has a good creditworthiness.
If a customer is denied a credit card, the team must be able to provide a reason for it. This means that the model must provide easily interpretable directions.

</details>
