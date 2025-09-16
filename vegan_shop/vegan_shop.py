import input as inp
from item import Item
from profit import ProfitManager
from shopping_list import ShoppingList
from wh_csv import Wh_csv




class VeganShop():
    '''
    Class with methods to manage the functionalities of the shop
    '''
    
    def __init__(self, _profit_manager= ProfitManager(), _warehouse_manager= Wh_csv(), _bag= ShoppingList()):
        '''
        Initialize the shop with the managers of the warehouse and the profits
        '''
        self.profit_manager = _profit_manager
        self.warehouse_manager = _warehouse_manager
        self.profit_manager = _profit_manager
        self.profit_manager.read_profit()
        self.bag = _bag   

     
    def show_list(self):
        '''
        Show the list of the products in the warehouse
        '''
        list_products = self.warehouse_manager.read_prod()  
        print('PRODOTTO\tQUANTITA\'\tPREZZO')
        for p in list_products:
            p.print_item(sp=True)    
        print("") 
        return True
         

    def add_product(self):
        '''
        Add a product to the warehouse
        '''
        name = inp.check_str('Nome del prodotto: ')
        quantity = inp.control_num('Quantità: ', type=int)
        prod_found = self.warehouse_manager.check_product(name)

        if prod_found.index is not None:
            product = prod_found
            product.quantity = quantity    
            self.warehouse_manager.update_product(product, add=True)
        else:
            purchase_price = inp.control_num('Prezzo di acquisto: ', float)
            sale_price = inp.control_num('Prezzo di vendita: ', float)
            product = Item(name, quantity, purchase_price, sale_price)
            self.warehouse_manager.insert_new_product(product)
                    
        return print("AGGIUNTO: %d X %s\n" % (product.quantity, product.name))
    
    
    def buy(self):
        '''
        Take in input the request of a series of products and return a list of the products
        '''
        while True:
            product = Item()
            name = inp.check_str('Nome del prodotto: ')
            quantity = inp.control_num('Quantità: ', type=int)
            
            prod_found = self.warehouse_manager.check_product(name)
            prod_in_list = self.bag.get_item(name)
            if prod_in_list is not None:
                prod_found.q_disp = prod_in_list.q_disp
            else:
                prod_found.q_disp = prod_found.quantity
              
            if prod_found.index is None:
                print("Il prodotto %s non è presente in magazzino." % name)    
            else:
                if prod_found.q_disp >= quantity:
                    product = prod_found
                    product.quantity = quantity
                    self.bag.add_to_sl(product)
                else:
                    print("Non ci sono abbastanza prodotti in magazzino, sono rimasti solo %d di %s." % (prod_found.q_disp, prod_found.name))
                    hold = inp.check_yes_no('Vuoi acquistare tutti i prodotti rimasti? (si/no): ')
                    if hold == 'si':
                        product = prod_found
                        product.quantity = prod_found.q_disp
                        self.bag.add_to_sl(product) 

            go = inp.check_yes_no('Aggiungere un altro prodotto? (si/no): ')
            if go == 'no':
                break
            elif go == 'si':
                continue
            
        return True
                
                       
    def checkout(self):
        '''
        Calculate the total sale and the total cost of the shopping list and print the receipt
        '''
        self.bag.calculate_total()

        if self.bag.list == []:
            print("Carrello vuoto.")
        else:
            print("VENDITA REGISTRATA")
            self.bag.print_list()
            self.profit_manager.update_profit(self.bag)
            
        print("Totale: \u20AC%.2f\n" % self.bag.total_sale)
        self.warehouse_manager.update_product_from_sale(self.bag)
        self.bag.empty_bag()
        return True
    
    
    def show_profit(self):
        '''
        Print on screen the gross and net profit
        '''
        self.profit_manager.print_profit()
        return True
    
    
    def menu(self):
        '''
        Show the menu of the possible actions with the call AIUTO 
        '''
        print("I comandi disponibili sono i seguenti:")
        print("\t- aggiungi: aggiungi un prodotto al magazzino")
        print("\t- elenca: elenca i prodotto in magazzino")
        print("\t- vendita: registra una vendita effettuata")
        print("\t- profitti: mostra i profitti totali")
        print("\t- aiuto: mostra i possibili comandi")
        print("\t- chiudi: esci dal programma\n")
        return True
         
         
    def close(self):
        '''
        Close the program
        '''
        print("Bye bye")
        return exit()