import csv
from item import Item

class Wh_csv():
    '''
    Class that has the methods to manage the csv warehouse file 
    '''
    
    def __init__(self, _file = 'warehouse.csv'):
        '''
        Inizialize the class with the name of the file csv to manage the warehouse
        Check if the file is empity and write the header
        '''
        self.file = _file
        with open(self.file, mode='r+' ,newline='') as csvfile:   
                reader = csv.reader(csvfile)
                writer = csv.writer(csvfile)
                header = ["name","quantity","purchase_price","sale_price"]
                first_row = next(reader,None)
                if first_row and set(first_row) == set(header):
                    return
                else:
                    writer.writerow(header)
 
    def read_prod(self):
        '''
        Read the file and return the list of Item in the warehouse
        '''
        list_prod = []
        with open(self.file, mode='r' ,newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"]
                quantity = int(row["quantity"])
                p_price = float(row["purchase_price"])
                s_price = float(row["sale_price"])
                product = Item(name, quantity, p_price, s_price)
                list_prod.append(product)
            csvfile.close()
        return list_prod


    def check_product(self, p_name):
        '''
        Check if the product is already in the warehouse
        '''
        product = Item()
        with open(self.file, mode='r' ,newline='') as csvfile:   
            r = csv.DictReader(csvfile)                                 
            for i, row in enumerate(r):
                if row["name"] == p_name:
                    product.index = i
                    product.name = row["name"]
                    product.quantity = int(row["quantity"])
                    product.purchase_price = float(row["purchase_price"])
                    product.sale_price = float(row["sale_price"])
                    break
            csvfile.close()
        return (product)
    
    
    def insert_new_product(self, product):
        '''
        Insert the new product in the warehouse
        '''
        with open(self.file, mode='r+' ,newline='') as csvfile:   
                reader = csv.DictReader(csvfile)
                writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
                row = product.__dict__()
                writer.writerow(row)
                csvfile.close()
        return True
       
        
    def update_product(self, product, add=False, remove=False):
        '''
        The product is already in the warehouse, update the quantity
        '''
        rows = []          
        with open(self.file, mode='r', newline='') as csvfile:    
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            old_quantity = int(rows[product.index]['quantity'])
            if add:
                rows[product.index]['quantity'] = old_quantity + product.quantity
            elif remove:
                rows[product.index]['quantity'] = old_quantity - product.quantity
            csvfile.close()
                
        with open(self.file, mode='w', newline='') as csvfile:     
            writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)  #decision to maintain also the products with quantity 0
                                    #ON CLIENT REQUEST: implement a method to give the possibility to change the prices
            csvfile.close()
        return True      
    
    
    def update_product_from_sale(self, sl):
        for product in sl.list:
            self.update_product(product, remove=True)
        return True