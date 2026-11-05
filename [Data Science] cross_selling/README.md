# Insurance Cross-Selling

Predicting which health-insurance customers are likely to accept an offer for an
additional vehicle insurance policy, to help target marketing campaigns.
The original assignment is kept at the bottom of this page.

## Tech stack

- **Language**: Python 3.12+
- **Data handling**: pandas, NumPy, SciPy (statistical tests)
- **Visualisation**: Matplotlib, seaborn
- **Modelling**: scikit-learn (pipelines, preprocessing, Logistic Regression, KNN,
  Naive Bayes, Decision Tree, Random Forest), XGBoost
- **Class imbalance**: imbalanced-learn (random over/undersampling, SMOTE,
  resampling inside pipelines), class weights
- **Feature selection**: mutual information, XGBoost feature importance (gain)
- **Environment**: Jupyter notebook (ipykernel), pinned dependencies in `requirements.txt`

## Results

Final model: **XGBoost with random oversampling** (minority class oversampled to a
0.6 ratio), evaluated on a stratified hold-out test set (30%, 114,333 customers,
14,013 of them positive).

| Metric (class 1 = accepts the offer) | Value |
|---|---|
| Precision | 0.318 |
| Recall | 0.805 |
| F1 | 0.456 |
| Accuracy | 0.764 |
| ROC-AUC | 0.856 |

Best configuration of each algorithm, on the same test set:

| Model | Configuration | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| **XGBoost** | oversampling 0.6 | 0.32 | 0.80 | 0.46 | 0.86 |
| Logistic Regression | SMOTE 0.3 + undersampling 0.5 | 0.31 | 0.76 | 0.44 | 0.84 |
| Random Forest | undersampling 1.0 | 0.28 | 0.84 | 0.42 | 0.83 |
| Gaussian Naive Bayes | SMOTE 1.0 | 0.25 | 0.98 | 0.40 | 0.82 |
| Decision Tree | undersampling 1.0 | 0.26 | 0.70 | 0.38 | 0.71 |

The positive class is 12.3% of the data (imbalance about 1:7), so accuracy alone is
not informative. The final model was chosen as the best compromise between recall,
F1 and ROC-AUC.

## Business case (illustrative)

Hypothetical campaign on 100,000 customers, 12% of whom would accept the offer,
with an assumed cost of €5 per contact and €100 revenue per conversion. These
figures are assumptions, not data from the source.

| | Contact everyone | Contact model-selected customers |
|---|---|---|
| Customers contacted | 100,000 | about 30,000 |
| Conversions | 12,000 | about 9,660 |
| Cost | €500,000 | €150,000 |
| Revenue | €1,200,000 | €966,000 |
| Net gain | €700,000 | €816,000 |
| ROI | 140% | 544% |

The result depends on the assumed values, but on those assumptions the cost reduction is substantial (70% fewer contacts), resulting in a higher profit and ROI making the campaign much more efficient. This illustrates how the model, by prioritizing likely responders, can significantly optimize marketing efforts and maximize profitability, especially when the contact budget or capacity is limited.

## Approach

1. **EDA**: distributions, correlations (Pearson, Cramér's V, Kruskal-Wallis) and
   hypothesis tests. The target is imbalanced and the strongest signals are
   `Previously_Insured`, `Vehicle_Damage`, `Age` and `Policy_Sales_Channel`.
2. **Preprocessing**: `id` dropped, numeric features standardised, categorical
   features one-hot encoded inside the pipeline.
3. **Evaluation protocol**: stratified 70/30 hold-out split, chosen over
   cross-validation for computational cost.
4. **Baselines**: Logistic Regression, KNN, Gaussian Naive Bayes, Decision Tree,
   Random Forest and XGBoost.
5. **Imbalance handling**: random oversampling, random undersampling, SMOTE, SMOTE
   plus undersampling (ratios from 0.4 to 1.0, applied only to the training data
   inside the pipeline) and class weights. Resampling gave better results than class
   weights for recall, the main objective.
6. **Overfitting check**: train versus test metrics for the best configuration of
   each algorithm. Decision Tree and Random Forest overfit; Logistic Regression,
   XGBoost and Naive Bayes generalise well.
7. **Feature selection**: three variants (mutual information, mutual information
   with grouped `Policy_Sales_Channel` and `Region_Code`, XGBoost gain). Recall
   improved for Decision Tree and Random Forest, but their F1 and ROC-AUC stayed
   below the best model trained on all features.
8. **Final model**: XGBoost with oversampling 0.6, plus the cost-benefit estimate above.

## Repository content

- `cross_selling.ipynb`: full analysis, with outputs saved.
- `requirements.txt`: pinned versions used for the results.

## How to run

Python 3.12 or later is required.

```bash
python -m venv venv
venv\Scripts\activate        # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

Open the notebook and run all cells. The dataset is downloaded from a public URL.

## Limitations and next steps

- **Model selection and final evaluation share the same test set.** The candidate
  configurations were compared on the same hold-out set that reports the final
  figures, so the reported metrics may be slightly optimistic. A separate validation
  set or cross-validation would give a more robust estimate.
- **Primary metric.** Recall is the stated priority, but the final model was chosen
  weighing recall together with F1 and ROC-AUC. Gaussian Naive Bayes has the highest
  recall, with much lower precision.
- **No hyperparameter tuning or cross-validation.** Both are listed as next steps in
  the notebook.
- **Possible extensions.** Models are compared at a single decision threshold (0.5).
  A precision-recall curve comparison between models, and a decision threshold
  optimised on validation data according to the cost structure of the campaign,
  would allow comparing the models at the same operating point and choosing the
  cutoff explicitly.
- **Business case.** Costs and revenues are hypothetical, and the conclusion depends
  on them (see the break-even on real market data).
- **Protected attributes.** Gender and age are model features; a fairness analysis
  has not been done and would be advisable before any real use.

---

<details>
<summary>Original assignment</summary>

## Company Background
**Company:** AssurePredict  
**Sector:** Insurance and Risk Management  

AssurePredict is a leading insurance company specialized in innovative risk management solutions.  
This project aims to build a **predictive model** capable of identifying potential cross-selling opportunities among existing customers — specifically, identifying clients who may be interested in purchasing an **additional vehicle insurance policy**.  

---

## Project Objective
The goal is to develop a **machine learning model** that predicts whether customers, who currently hold a **health insurance policy**, might also be interested in subscribing to a **vehicle insurance policy**.  

This model will help AssurePredict:  
- Improve cross-selling strategies  
- Increase market penetration  
- Enhance marketing efficiency  

---

## Business Value for AssurePredict
- **Higher Conversion Rates**: Increase the sales rate of vehicle insurance policies.  
- **Marketing Optimization**: Target campaigns toward customers most likely to purchase.  
- **Reduced Marketing Costs**: Avoid inefficient campaigns through precise targeting.  

---

## Dataset
The dataset can be downloaded here: 👉 [insurance_cross_sell.csv](https://proai-datasets.s3.eu-west-3.amazonaws.com/insurance_cross_sell.csv)  

It includes detailed customer and insurance behavior data with the following features:  

- **id**: unique customer identifier  
- **Gender**: customer gender  
- **Age**: customer age  
- **Driving_License**: 1 if the customer holds a driving license, 0 otherwise  
- **Region_Code**: unique code for customer’s region  
- **Previously_Insured**: 1 if the customer already has vehicle insurance, 0 otherwise  
- **Vehicle_Age**: customer’s vehicle age  
- **Vehicle_Damage**: 1 if the customer has had accidents/damage in the past, 0 otherwise  
- **Annual_Premium**: annual insurance premium paid by the customer  
- **PolicySalesChannel**: sales channel used (email, phone, in-person, etc.)  
- **Vintage**: number of days the customer has been insured with AssurePredict  
- **Response**: target variable (1 = accepted the cross-sell offer, 0 = rejected)  

---

## Project Steps

### 1. Dataset Exploration
Perform an exploratory analysis to:  
- Examine the distribution of the target variable **Response** (identify class imbalance).  
- Explore relationships between key variables such as **Annual_Premium**, **Vehicle_Age**, **Previously_Insured**, and **Response**.  

**Added Value:** Early exploration reveals hidden patterns and critical factors influencing model performance.  

---

### 2. Handling Class Imbalance
The **Response** variable is likely imbalanced (many more customers reject than accept the cross-sell).  
To address this:  
- **Class Weights**: penalize the majority class in the model  
- **Oversampling / Undersampling**: balance the dataset to improve generalization  

**Added Value:** Correctly handling imbalance avoids models with high false negatives, ensuring better prediction accuracy.  

---

### 3. Building the Predictive Model
Train machine learning algorithms to predict whether a customer will respond positively to the cross-sell offer.  

**Added Value:** The model helps AssurePredict precisely identify customers more likely to purchase an additional policy, maximizing marketing ROI.  

---

## Conclusion
This project enables AssurePredict to leverage **machine learning** for effective and targeted cross-selling.  
A data-driven approach ensures:  
- Increased vehicle insurance sales  
- Reduced marketing costs  
- Higher customer satisfaction thanks to personalized offers  

---

## Key Considerations
Be mindful of class imbalance when training the model:  
- Apply **class_weight** to penalize the majority class  
- Experiment with **oversampling / undersampling** strategies


</details>