class Item():
    '''
    Class that represents a product
    '''
    def __init__(self, _name='', _quantity=0, _purchase_price=0, _sale_price=0, _index=None):
        self.name = _name
        self.quantity = _quantity
        self.q_disp = _quantity
        self.purchase_price = _purchase_price
        self.sale_price = _sale_price
        self.index = _index
    
    
    def __dict__(self):
        '''
        Return the dictionary of the product
        '''
        return {"name": self.name, "quantity": int(self.quantity), "purchase_price": float(self.purchase_price), "sale_price": float(self.sale_price)}
    
    
    def print_item(self, n=True, q=True, pp=False, sp=False):
        '''
        Print the item with the selected parameters 
        Allign the columns based on the length of the name
        '''
        attr_to_print = []
        if n:
            attr_to_print.append(f"{self.name}")
        if q:
            attr_to_print.append(f"{self.quantity}")
        if pp:
            attr_to_print.append(f"\u20AC{float(self.purchase_price): .2f}")
        if sp:
            attr_to_print.append(f"\u20AC{float(self.sale_price): .2f}")
        
        if len(self.name) >= len("PRODOTTO"):
            print(f'{attr_to_print[0]}', end="\t")
            print("\t\t".join(attr_to_print[1:]))
        else:
            print("\t\t".join(attr_to_print))
        return True