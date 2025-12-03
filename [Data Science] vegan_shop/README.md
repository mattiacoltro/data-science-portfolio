# Software for vegan product store
BioMarket s.a.s hires you to develop a small management software for their new store. 
The software must have the following features: 
- Register new products, with name, quantity, sale price, and purchase price.
- List all available products.
- Record sales.
- Display gross and net profits.
- Display a help menu with all available commands.
  
The software is text-based, so it can be used from the command line.

## Project Structure
- class *Item*: to manage the items and their characteristics
- class *ProfitManager*: to manage the calculations
- class *ShoppingList*: to manage the shopping process
- class *VeganShop*: to manage the different functionalities of the shop
- class *Wh_csv*: to manage the warehouse
- main: orchestrator of the process with command line interface

## Technology
- Python
