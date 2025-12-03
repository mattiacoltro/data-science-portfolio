# Prediction of creditworthiness
You have been hired by Pro National Bank as a data scientist, and your first task is to create a model that can estimate the creditworthiness of customers, in order to help the dedicated team understand whether or not to accept credit card applications.


## Tools & Technologies 
- Python (pandas, numpy, scikit-learn, imbalanced-learn)
- Exploratory Data Analysis (EDA)
- Supervised Machine Learning (Logistic Regression, Random Forest, XGBoost, KNN, Naive Bayes, Decision Tree, LightGBM)
- Evaluation Metrics: Precision, Recall, F1-Score, ROC-AUC


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
