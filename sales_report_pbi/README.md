# Sales Management for TechMarket S.p.A. Stores

## Project Context
TechMarket S.p.A. is one of the leading retail chains for electronics products in Italy, with stores distributed throughout the country.  
The company needs to manage huge amounts of data coming from each store and generate complete and detailed reports on the sales of its key products.  

For this reason, TechMarket has decided to invest in an advanced sales reporting solution, capable of aggregating and visualizing complex data in a clear and navigable way.  

You have been hired to implement a reporting system that processes sales data and provides detailed insights for decision-makers.  
The report will allow monitoring of sales, product performance, the effectiveness of promotions, and the performance of each individual store.  

---

## Project Goal
The objective is to create an interactive report that enables TechMarket managers to:

- Visualize monthly sales, considering discounts, units sold, and prices.  
- Analyze sales for each city.  
- Monitor sales performance by product.  
- Obtain a complete overview of data from each store.  

Additionally, it will be necessary to:  
- Create a page that accounts for product returns to calculate **net sales**, providing a more accurate view of performance.  

---

## Added Value
The developed report will provide TechMarket with a significant competitive advantage by enabling:

- **Data-driven decisions**: Executives will have access to accurate and up-to-date information for targeted strategic decisions. They will be able to identify the best-selling products during specific periods and the cities with the highest performance.  
- **Optimization of sales and promotions**: Thanks to detailed data, promotional campaigns can be optimized by identifying which discounts and offers have the greatest impact on sales.  
- **Real-time monitoring of stores**: Managers will be able to track each store’s performance, improving inventory and human resource management.  
- **Return management**: Integrating return data will allow calculation of net sales, offering a more realistic view of store performance.  
- **Interactivity and navigation**: The ability to navigate across pages with bookmarks and interactive buttons will make the report easy to use, even for non-technical users.  

---

## Project Phases

### 1. Data Loading
- **Sales Data**: Files will be loaded from the [DATI folder](https://drive.google.com/drive/folders/1iYuYuvip3NwvB2LK9SAbKWZP-aZ5IObL), containing information on sales across various stores during 2014.  
- **Additional Data**: Files from the **DATI NEGOZI** folder will be loaded, containing information about stores, products, and Italian provinces.  

---

### 2. Data Transformation
Data will be transformed and merged using the **Query Merge function**, combining tables appropriately to obtain details such as **Unit Price** and **Product Description** for each `Product_ID`.  

---

### 3. Interactive Report Creation
The report will include several pages, each with tailored visualizations:

- **Monthly Sales**: A page displaying total sales per month, considering discounts, units sold, and prices.  
- **Units Sold by City**: Analysis of units sold in each city with a TechMarket store.  
- **Product Details**: A page showing relevant information and performance metrics for each product.  
- **Store Information**: An overview of each store, merging store and sales data to provide a complete performance picture.  

---

### 4. Returns Management
Return data will be loaded, and a new page will be created to display a table showing **net sales** (excluding return transactions) for January and February.  
This will give a more accurate view of TechMarket’s net performance.  

---

### 5. Navigation and Interactivity
The report will be fully navigable, with buttons to switch between pages.  
Bookmarks will be added for quick access to key report sections.  

---

## Conclusion
The **TechMarket S.p.A. sales management project** represents a significant opportunity to optimize sales operations and improve business decision-making.  

The added value lies in:  
- Enhanced visibility of sales data.  
- The ability to make more informed strategic decisions.  
- Optimization of resources at the store level.  

Integrating return data also provides a **realistic view of net sales**, improving reporting accuracy and strengthening the company’s ability to adapt quickly to market changes.  

## Technology 
Excel
PowerBI
