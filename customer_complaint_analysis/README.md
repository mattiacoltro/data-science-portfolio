# Consumer Complaint Analysis

The project was commissioned by FinServ Solutions, a company specializing in software solutions for managing customer complaints in the financial sector. 
The objective is to improve the effectiveness of customer complaint analysis by restructuring and customizing a spreadsheet in order to optimize access to information and the decision-making process.

## Dataset
[Link to dataset](https://github.com/Profession-AI/progetti-excel/raw/main/Analisi%20dei%20reclami%20dei%20consumatori/customers_complaints_assignment.xlsx)

## Motivation
The company has noticed that the current structure of the spreadsheet used for complaint management is inefficient, making it difficult to read data, extract insights, and perform geographical analysis. A targeted review of the spreadsheet will improve the visibility of critical data, enabling faster identification of problems and optimizing the company's response to customers. In addition, a graphical and functional reorganization will allow the customer service team to operate with greater agility.

## Expected Added Value
- Improved geographic analysis: The creation of a tab dedicated to geographic insights will facilitate the identification of areas with the highest number of complaints, enabling targeted actions.
- Greater efficiency in decision-making: Thanks to the addition of a statistics tab and the ability to filter data, the team will be able to quickly identify the most frequent issues, enabling a faster and more appropriate response.
- Optimization of response time: The new structure will automatically highlight complaint resolution times, providing more effective monitoring of company performance.

## Request
To implement the project, you will need to modify the attached spreadsheet so that it has the following structure:

### 1. First tab or sheet

Name: “Consumer complaints”

Style: 
- The first header row is in Comics Sans MS font, size 12pt and blue, framed on all four sides with a double border.
- Each cell other than the title is framed on all four sides in black with a thin border.
- There are no empty cells outside the table (they are colored white with no borders around the rows and columns containing the actual data).
- The dates (Date received and Date sent to company columns) are in dd/mm/yy format.

Content: 
- A column at the bottom containing the number of actual days between the date of sending and the date of receipt of the communication.
- The spreadsheet contains rows sorted in ascending order by the value in the Complaint ID column.
- There is a filter on the Date received column, which allows only rows with a date prior to August 8, 2016, to be displayed.


### 2. Second tab or sheet
   
Name: “Geographical insights”

Style: 
- The first header row is in Comics Sans MS font, size 12pt and blue, framed on all four sides with a double border.
- Each cell that is not part of the title is framed on all four sides in black with a thin border.
- There are no empty cells outside the table (they are colored white with no borders around the rows and columns containing the actual data).
- The header row contains the following titles:
  - Number of complaints per state
  - Percentage of complaints per state
  - There is a header column containing all the state abbreviations in the “Consumer complaints” tab

Content: 
- Column B shows the number of complaints in the main tab broken down by state. (Hint: use the COUNTIF function).
- Column C shows the percentage (rounded to the nearest whole number) of complaints in the main tab broken down by state. The cell is green if the percentage is less than 2%, red otherwise. (Hint: conditional formatting).

### 3. Third tab or sheet

Name: “Statistical insights”

Style: 
- The first header row is in Comics Sans MS font, size 12pt and blue, framed on all four sides with a double border.
- Each cell other than the title is framed on all four sides in black with a thin border.
- There are no empty cells outside the table (they are colored white with no borders around the rows and columns containing the actual data).
- The header row contains the following titles: Distinct issues

Contents: 
- Column A lists all possible reasons for complaints (distinct values from the Issues column of the main tab).
- Cell B7 shows the mode (most frequent) value among all categories of complaints. (Hint: count the occurrences of the various issues and find the mode among the numerical values).

## Technology
Excel


