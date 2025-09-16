# Bank Customers Analysis

The company Banking Intelligence wants to develop a supervised machine learning model to predict the future behavior of its customers, 
based on transactional data and product ownership characteristics. 
The aim of the project is to create a denormalized table with a series of indicators (features) derived from the tables available in the database, 
which represent the behavior and financial activities of customers.

## Objective
Our goal is to create a feature table for training machine learning models, enriching customer data with various indicators calculated from their transactions and accounts. 
The final table will refer to the customer ID and contain both quantitative and qualitative information.

## Added Value
The denormalized table will allow advanced behavioral features to be extracted for training supervised machine learning models, providing numerous benefits for the company:
- *Predicting customer behavior*: By analyzing transactions and product ownership, behavior patterns can be identified that are useful for predicting future actions such as purchasing new products or closing accounts.
- *Reduction in churn rate*: Using behavioral indicators, a model can be built to identify customers at risk of churn, allowing for timely intervention by the marketing team.
- *Improved risk management*: Segmentation based on financial behavior allows you to identify high-risk customers and optimize credit and risk strategies.
- *Personalization of offers*: The extracted features can be used to personalize product and service offers based on the habits and preferences of individual customers, thereby increasing customer satisfaction.
- *Fraud prevention*: By analyzing transactions by type and amount, the model can detect behavioral anomalies indicative of fraud, improving security and prevention strategies.

These benefits will lead to an overall improvement in business operations, enabling greater efficiency in customer management and sustainable business growth.

## Database Structure
The database (which you can [download here](https://drive.google.com/file/d/1l54AQ2xGgP-1X6AU8nF53IOCt83I_h88/view)) consists of the following tables:

**Customer**: contains personal information about customers (e.g., age).
**Account**: contains information about the accounts held by customers.
**Account_type**: describes the different types of accounts available.
**Transaction_type**: contains the types of transactions that can take place on the accounts.
**Transactions**: contains details of transactions made by customers on various accounts.

## Indicators to be Calculated
The indicators will be calculated for each individual customer (referenced by customer_id) and include:

### Basic indicators
- Customer age (from customer table).
### Transaction indicators
- Number of outgoing transactions on all accounts.
- Number of incoming transactions on all accounts.
- Total amount transacted out on all accounts.
- Total amount transacted in on all accounts.

### Account indicators
- Total number of accounts held.
- Number of accounts held by type (one indicator for each account type).
- Transaction indicators by account type
- Number of outgoing transactions by account type (one indicator per account type).
- Number of incoming transactions by account type (one indicator per account type).
- Outgoing transaction amount by account type (one indicator per account type).
- Incoming transaction amount by account type (one indicator per account type).

## Technology
SQL
