# Texas Real Estate Market Analysis

## My Rpubs profile
The project is on my [Rpubs profile](http://rpubs.com/mattia11coltro/)

## Tools & Technologies
- **R** (base functions, dplyr, ggplot2)  
- **Statistical methods** for descriptive and inferential analysis  
- **Data visualization** with ggplot2  

## Project Description
**Texas Realty Insights** aims to analyze real estate market trends across Texas using historical property sales data.  
The objective is to provide **statistical and visual insights** to support strategic decision-making in property sales and listing optimization.  

---

## Project Goals
- Identify and interpret historical real estate sales trends in Texas  
- Assess the effectiveness of property listing marketing strategies  
- Provide graphical representations of data, highlighting the distribution of prices and sales across cities, months, and years  

---

## Added Value
The proposed statistical analysis will help **Texas Realty Insights** optimize market strategies by:  
- Identifying cities with growth opportunities  
- Evaluating the effectiveness of property listings over time  
- Enabling data-driven decisions for improved sales management in the Texas real estate market  

---

## Dataset
[Download dataset](https://drive.google.com/file/d/1O4If8876MTwstkrZX0BqpQ_BxcsIMEko/view?usp=sharing)

The dataset contains the following variables:  
- **city**: city of reference  
- **year**: reference year  
- **month**: reference month  
- **sales**: total number of sales  
- **volume**: total sales value (in millions of dollars)  
- **median_price**: median sales price (in dollars)  
- **listings**: total number of active listings  
- **months_inventory**: time needed to sell all current listings (in months)  

---

## Project Steps

### 1. Variable Analysis
- Identify and describe the type of statistical variables in the dataset  
- Handle variables with a time dimension  
- Comment on the types of analysis that can be applied to each variable  

### 2. Measures of Central Tendency, Variability, and Shape
- Compute descriptive statistics (mean, median, variance, skewness, etc.) where relevant  
- For categorical variables, create frequency distributions  
- Provide a brief commentary  

### 3. Identifying Variables with Higher Variability and Skewness
- Determine which variable has the **highest variability**  
- Identify the variable with the **most skewed distribution**  
- Explain the reasoning with statistical considerations  

### 4. Creating Classes for a Quantitative Variable
- Select a quantitative variable (e.g., *sales* or *median_price*)  
- Divide it into classes and create a frequency distribution  
- Represent the data with a bar chart  
- Calculate the **Gini heterogeneity index** and discuss the results  

### 5. Probability Calculations
- Probability that a random row corresponds to **Beaumont**  
- Probability of the row being from **July**  
- Probability of the row being from **December 2012**  

### 6. Creating New Variables
- Create a new column calculating the **average property price**  
- Add a column measuring the **effectiveness of property listings**  
- Provide commentary and discussion on results  

### 7. Conditional Analysis
- Use **dplyr** (or base R) to perform conditional statistical analysis by **city, year, and month**  
- Generate summaries (mean, standard deviation) and graphical representations  

### 8. Data Visualizations with ggplot2
- **Boxplots**: compare median price distribution across cities  
- **Bar charts**: compare total sales across months and cities  
- **Line charts**: compare sales trends across historical periods  
- Include customized ggplot2 visuals with appropriate commentary  

### 9. Conclusions
Summarize the findings, highlighting key emerging trends and statistical insights.  
Provide **recommendations** for real estate sales strategy improvements.  

---

## Operational Notes
- Use **boxplots** to compare distributions of median price across cities and sales volume across years  
- Create **stacked bar charts** (and normalized versions) to compare monthly sales across cities  
- Explore **geom_bar() vs geom_col()** differences  
- Advanced: incorporate the **year** variable in bar charts without cluttering the visuals  
- Create **line charts** for selected variables to compare cities and time periods (expect some messy outputs at first, refine gradually)  


