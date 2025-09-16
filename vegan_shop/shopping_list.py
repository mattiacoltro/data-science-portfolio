class ShoppingList():
    '''
    Class that represents the shopping list
    '''
    def __init__(self, _list=[], _total_cost=0, _total_sale=0):
        self.list = _list
        self.total_cost =  _total_cost
        self.total_sale =  _total_sale
        
        
    def get_item(self, name_item):
        '''
        Return the item with the name passed as argument
        '''
        for p in self.list:
            if p.name == name_item:
                return p
        return None
    
    
    def add_to_sl(self, product):
        '''
        Take in input the request of a series of products and return a list of the products
        '''
        product.q_disp = product.q_disp - product.quantity
        self.list.append(product)
        return True
        
        
    def calculate_total(self):
        '''
        Calculate the total cost and the total sale of the shopping list
        '''
        for product in self.list:
            self.total_cost += float(product.purchase_price * product.quantity)
            self.total_sale += float(product.sale_price * product.quantity)
        return True
       
        
    def print_list(self):
        '''
        Print the shopping list
        '''
        for p in self.list:
            print(f'- {p.quantity} X {p.name}: \u20AC{float(p.sale_price): .2f}')
        return True    
    
          
    def empty_bag(self):
        '''
        Empty the shopping list
        '''
        self.list = []
        self.total_cost = 0
        self.total_sale = 0
        return True