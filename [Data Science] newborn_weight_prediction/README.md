# Statistical Model for Predicting Neonatal Birth Weight

## My Rpubs profile
the project is public on my [Rpubs profile](http://rpubs.com/mattia11coltro/)

## Tools & Technologies
- **R** (descriptive statistics, regression, model selection, visualization)  
- **Statistical tests** (t-test, ANOVA, chi-square, regression diagnostics)  
- **ggplot2** for customized visualizations  

## Dataset
👉 [Download Dataset](https://drive.google.com/file/d/1ChfwftuOSH-WLIto1AvV-sQIksGeTq/view)  


## Business Context
**Company:** Neonatal Health Solutions  
**Objective:** Develop a statistical model capable of accurately predicting neonatal birth weight based on clinical variables collected from three hospitals.  

The project aims to:  
- Improve the management of high-risk pregnancies  
- Optimize hospital resources  
- Ensure better neonatal health outcomes  

This initiative aligns with the growing focus on **preventing neonatal complications**. Being able to predict birth weight represents a crucial opportunity to improve clinical planning and reduce risks associated with problematic births, such as preterm deliveries or low-birth-weight infants.  

### Key Benefits
- **Improved Clinical Predictions**  
  Birth weight is a critical indicator of newborn health. An accurate predictive model enables medical staff to intervene early in case of anomalies, reducing perinatal complications such as respiratory difficulties or hypoglycemia.  

- **Optimization of Hospital Resources**  
  Anticipating which newborns may require intensive care helps hospitals allocate staff and technology more effectively, reducing operational costs and improving neonatal intensive care unit (NICU) planning.  

- **Risk Prevention and Identification**  
  The model will highlight factors that negatively impact neonatal weight (e.g., maternal smoking, multiple pregnancies, advanced maternal age). This information is key for preventive measures and personalized pregnancy management.  

- **Evaluation of Hospital Practices**  
  By comparing the three hospitals involved, the company can identify differences in clinical outcomes (e.g., higher incidence of C-sections in one facility). This supports quality monitoring and the harmonization of protocols across hospitals.  

- **Support for Strategic Planning**  
  Insights and predictions can inform clinical and strategic decision-making, helping the company implement public health policies that positively affect neonatal mortality and morbidity rates.  

---

## Project Details

### 1. Data Collection and Dataset Structure
Data were collected on **2,500 newborns** from three hospitals. The dataset includes:  
- **Mother’s age** (in years)  
- **Number of pregnancies**  
- **Maternal smoking** (binary: 0 = non-smoker, 1 = smoker)  
- **Gestation duration** (in weeks)  
- **Newborn weight** (in grams)  
- **Head length and diameter** (from birth or ultrasound measurements)  
- **Delivery type** (natural or C-section)  
- **Hospital of birth** (Hospital 1, 2, or 3)  
- **Newborn’s sex** (M = male, F = female)  

The main goal is to identify the most predictive variables for birth weight, with a particular focus on **maternal smoking** and **gestation weeks** as indicators of potential premature births.  

---

### 2. Analysis and Modeling

#### Preliminary Analysis
- Perform descriptive analysis of all variables  
- Identify outliers or anomalies  
- Test hypotheses, including:  
  - Higher C-section rates in some hospitals  
  - Whether sample means (weight, length) differ significantly from population values  
  - Significant differences in anthropometric measures between sexes  

#### Regression Model Development
- Build a **multiple linear regression model** including relevant variables  
- Quantify the impact of each independent variable on birth weight  
- Explore interactions (e.g., longer gestation increases birth weight)  

#### Model Selection
- Apply model selection techniques (AIC, BIC)  
- Remove non-significant variables  
- Consider interaction terms and possible non-linear effects  

#### Model Evaluation
- Assess predictive power using **R²** and **Root Mean Squared Error (RMSE)**  
- Analyze residuals and influential values that may distort predictions  

---

### 3. Predictions and Results
Once validated, the model will be applied to real cases.  
**Example:** Estimate the weight of a newborn from a mother in her third pregnancy delivering at week 39.  

---

### 4. Visualizations
Use visual tools to communicate insights and highlight significant relationships:  
- Plots showing the effect of gestation weeks on birth weight  
- Comparisons of maternal smoking vs. non-smoking groups  
- Hospital-level comparisons for C-section incidence and newborn weight  

---

## Conclusions
The neonatal birth weight prediction project is a **key initiative for Neonatal Health Solutions**. By leveraging detailed clinical data and advanced statistical tools, this project will:  
- Improve prenatal care quality  
- Reduce neonatal risks  
- Optimize hospital resource efficiency  

It represents a **turning point for clinical practice** and provides a foundation for more informed, proactive healthcare policies.  
