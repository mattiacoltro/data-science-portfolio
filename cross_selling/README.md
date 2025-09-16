# Insurance Cross-Selling Project

## Tools & Technologies
- **Python** (pandas, numpy, scikit-learn, imbalanced-learn)  
- **Exploratory Data Analysis (EDA)**  
- **Supervised Machine Learning** (Logistic Regression, Random Forest, XGBoost, etc.)  
- **Evaluation Metrics**: Precision, Recall, F1-Score, ROC-AUC  

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
