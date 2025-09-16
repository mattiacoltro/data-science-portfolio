import re


def empty_string(s):
    '''
    Check if the string is empty
    '''
    if s == '':
        return True
    else:
        return False
    
    
def is_special_char(s):
    '''
    Check if the string contains special characters
    '''
    pattern = r"[^a-zA-Z0-9\s']"
    if re.search(pattern, s):
        return True
    else:
        return False


def is_number(s):
    '''
    Check if the string contains a number
    '''
    if any(char.isdigit() for char in s):
        return True
    else:
        return False


def check_str(text):
    '''
    Check the validity of the string
    '''
    while True:
        try:
            string = input(text).strip().lower()
            if empty_string(string):
                raise ValueError ("Input non valido, stringa vuota.")
            elif is_number(string):
                raise ValueError ("Input non valido, inserisci una stringa senza numeri.")
            elif is_special_char(string):
                raise ValueError ("Input non valido, inserisci una stringa senza caratteri speciali.")
            else:
                return string
        except ValueError as e:
            print(e)       
            
            
def control_num(text, type=float):
    '''
    Check the validity of the number, based on the type (int or float)
    '''
    while True:
        try:
            input_user = input(text)
            if type == int:
                number = int(input_user)
            else:
                number = float(input_user)
            if not number>0:
                raise ValueError
            return number

        except ValueError:
            if type == int:
                print("Inserisci un numero intero positivo.")
            else:
                print("Inserisci un numero positivo.")
                
                  
def check_yes_no(text):
    '''
    Check if the input is yes or no
    '''
    while True:
        try:
            input_user = input(text).strip().lower()
            if input_user == "si" or input_user == "no":
                return input_user
            else:
                raise ValueError("Input non valido. Inserisci 'si' o 'no'.")
        except ValueError as e:
            print(e)                