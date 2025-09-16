# Random Data and Linear Regression

## Project Context and Goal
In a data-driven company, the ability to generate and manipulate realistic data is essential to simulate real-world scenarios, support employee training, and test market hypotheses.  
This project focuses on creating a realistic dataset using a spreadsheet, with the goal of providing an effective tool to test statistical analysis techniques and predictive models.

---

## Project Description
The company aims to generate random but meaningful data regarding the imaginary population of **"Luggnagg"**.  
The focus is on a normal distribution for the population’s age, simulating a sample of 250 individuals.  
The spreadsheet will be structured in multiple tabs, each with a specific function reflecting the statistical concepts learned.

---

### 1. Dataset Generation
**Goal:** Create representative data of the population’s age and apply basic statistical techniques to analyze and interpret the results.  

**Input parameters:**  
- **Probability**: user-defined probability value.  
- **Mean**: average age value, defined by the user.  
- **StdDev**: standard deviation, representing the data dispersion around the mean.  

These parameters will be the basis for generating a normal distribution of ages for 250 individuals.

---

### 2. Dataset Manipulation
Once generated, the data will be manipulated to better explore its characteristics.  
The modifications will be spread across multiple tabs to simulate different analytical processes, useful for practicing various data manipulation and statistical analysis techniques.

---

## Spreadsheet Structure

### Tab 1: **Parameters**
**Goal:** Provide an interface to input the parameters of the normal distribution (probability, mean, standard deviation).  

**Style & Formatting:**  
- Header column: *Comic Sans MS*, 12pt, blue, double borders.  
- Value cells: thin black borders.  

---


### Tab 2: **Data**
**Goal:** Display the generated age data for 250 individuals and divide the population into random groups.  

**Style & Formatting:**  
- Column A: generated ages.  
- Column B: group assignment, randomly generated (integers 1–4).  
- Header row: *Comic Sans MS*, 12pt, blue, double borders.  

---

### Tab 3: **Sample**
**Goal:** Select a sub-sample from the generated data based on group membership.  

**Style & Formatting:**  
- Columns A–C: age, group, and selected sub-sample.  
- Use the conditional **IF** function to select values for a specific group (1, 2, 3, or 4).  

---

### Tab 4: **Statistical Insight**
**Goal:** Statistically analyze the selected sample by calculating key values such as standard deviation, expected value, and confidence interval.  

**Style & Formatting:**  
- Columns: **STDDEV, EXPECTED VALUE, COUNT, CONFIDENCE RATE, p parameter estimation, Confidence Interval**.  
- Text cell: detailed explanation of the obtained results and their statistical implications.  

---

### Tab 5: **(Un)correlated Variables**
**Goal:** Test the correlation between sample ages and other random variables (e.g., number of cats owned, partner’s age).  

**Style & Formatting:**  
- Columns: Sample data, Number of cats, Partner’s age.  
- Correlation calculated in a dedicated cell with explanation of results.  

---

### Tab 6: **Linear Regression**
**Goal:** Perform linear regression between individuals’ ages and their census rank.  

**Style & Formatting:**  
- Columns: Y (age), X (rank).  
- Scatterplot with linear regression calculated for participant 160.  

---

## Business Value of the Project
This project consolidates statistical concepts and practical skills in using spreadsheets for data analysis.  
Benefits for the company include:  

- **Simulation of real-world scenarios**: The generated data mimics a real population, providing a safe environment to test statistical and machine learning methods.  
- **Skills improvement**: A practical exercise for employees and data analysts to enhance their data manipulation and analysis skills.  
- **Data-driven decisions**: Insights from statistical analysis train employees to interpret and leverage data for evidence-based business decisions.  

---

## Conclusion
The creation and manipulation of realistic data through this project provides the company with a simulated learning environment that enables employees to effectively deepen their understanding of statistical concepts and analytical techniques.


## Technology
Excel
