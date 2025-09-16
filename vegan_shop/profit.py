import csv
class ProfitManager(): 
    '''
    Class with methods to manage the profits file
    '''
    
    def __init__(self, _file = 'profit.csv', _gross_profit=0, _net_profit=0):
        '''
        Inizialize the class with the name of the file csv to manage the profits
        Check if the file is empity and write the header
        '''
        self.file = _file
        self.total_gross = _gross_profit
        self.total_net = _net_profit
        with open(self.file, mode='r+' ,newline='') as csvfile:   
                reader = csv.reader(csvfile)
                writer = csv.writer(csvfile)
                header = ["gross","net"]
                first_row = next(reader,None)
                if first_row and set(first_row) == set(header):
                    return
                else:
                    writer.writerow(header)

    def read_profit(self): 
        '''
        Read the file with the profits
        '''
        with open(self.file, mode='r' ,newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.total_gross, self.total_net = float(row["gross"]), float(row["net"])
            csvfile.close()    
        return True
    
    
    def print_profit(self):
        '''
        Print the profits
        '''
        return print("Profitto: lordo= \u20AC%.2f netto= \u20AC%.2f \n" % (self.total_gross, self.total_net))
    
    
    def update_profit(self, shopping_list):
        '''
        Update the profits after a sale
        '''
        self.total_gross += shopping_list.total_sale
        self.total_net += (shopping_list.total_sale - shopping_list.total_cost)
        with open(self.file, mode='w', newline='') as csvfile:
            fieldnames = ['gross', 'net']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"gross": self.total_gross, "net": self.total_net})
            csvfile.close()
        return True