# Customer Segmentation for Targeted Marketing Campaigns

## Technology
Python

Machine Learning - Clustering

## Dataset
[Download the dataset](https://proai-datasets.s3.eu-west-3.amazonaws.com/credit_card_customers.csv)

## Project Overview
**FinTech Solutions S.p.A.**, a leader in the financial services industry, has decided to launch a new marketing campaign to promote its line of credit cards.  
To maximize campaign effectiveness, the company aims to **segment its customers into homogeneous groups** based on spending behavior and credit card usage.  

This segmentation will allow the company to **deliver personalized marketing campaigns** to each customer cluster, thereby maximizing ROI and improving the customer experience.  

---

## Project Objective
The main objective is to **develop a customer segmentation model** using the company’s dataset of credit card holders.  
The segmentation will help FinTech Solutions identify specific clusters of customers for **targeted marketing strategies**.  

---

## Dataset Description
The dataset includes the following variables:  

- **CUST_ID**: Unique identifier of the credit card holder (categorical)  
- **BALANCE**: Remaining account balance for purchases  
- **BALANCE_FREQUENCY**: Frequency of balance updates (0–1, where 1 = frequently updated)  
- **PURCHASES**: Total purchase amount  
- **ONEOFF_PURCHASES**: Highest single purchase amount  
- **INSTALLMENTS_PURCHASES**: Amount of purchases made in installments  
- **CASH_ADVANCE**: Cash advance amount  
- **PURCHASES_FREQUENCY**: Frequency of purchases (0–1, where 1 = frequent)  
- **ONEOFFPURCHASESFREQUENCY**: Frequency of one-off purchases (0–1)  
- **PURCHASESINSTALLMENTSFREQUENCY**: Frequency of installment purchases (0–1)  
- **CASHADVANCEFREQUENCY**: Frequency of cash advances  
- **CASHADVANCETRX**: Number of cash advance transactions  
- **PURCHASES_TRX**: Total number of purchase transactions  
- **CREDIT_LIMIT**: Maximum credit card limit per user  
- **PAYMENTS**: Total payments made by the user  
- **MINIMUM_PAYMENTS**: Minimum payments made by the user  
- **PRCFULLPAYMENT**: Percentage of full payments completed  
- **TENURE**: Length of credit card service (in years)  

---

## Added Value
Customer segmentation through clustering techniques provides several strategic benefits:  

- **Marketing Optimization**: Identify customer behaviors and preferences to create targeted promotional campaigns, improving response and conversion rates.  
- **Offer Personalization**: Develop tailored offers (e.g., credit limit increases, installment purchase discounts) that meet customer needs.  
- **Operational Efficiency**: Focus resources on the most profitable customer groups, optimizing acquisition and retention costs.  
- **Growth Opportunities**: Detect customer groups with growth potential (e.g., frequent installment users who don’t pay in full), enabling the company to propose additional financial products.  

---

## Project Phases
1. **Exploratory Data Analysis (EDA)**  
   - Understand variable distributions  
   - Handle missing data  
   - Assess necessary transformations  

2. **Data Preprocessing**  
   - Handle missing values (e.g., *MINIMUM_PAYMENTS*)  
   - Normalize and standardize quantitative variables (e.g., *BALANCE*, *PURCHASES*, *CASH_ADVANCE*)  

3. **Customer Segmentation with Clustering**  
   - Apply clustering algorithms (e.g., **K-Means**, **DBSCAN**)  
   - Evaluate clustering performance using **silhouette score** and **elbow method**  

4. **Cluster Interpretation**  
   - Analyze and describe clusters in terms of:  
     - Average spending (balance, one-off purchases, installment purchases)  
     - Payment habits (minimum vs. full payments)  
     - Card usage frequency (cash advances, purchase frequency)  

5. **Marketing Strategy Development**  
   - Build cluster-specific strategies, e.g.:  
     - Promotions to incentivize installment purchases  
     - Tailored offers for customers with high cash advance frequency, including additional financial services  

---

## Conclusion
Customer segmentation enables **FinTech Solutions S.p.A.** to improve marketing effectiveness by personalizing offers for specific user groups.  
This will lead to greater customer loyalty, increased transactions, and optimized usage of the company’s financial products.   
