from vegan_shop import VeganShop

def main():
    shop = VeganShop()
    while True:
        command = input("Inserisci un comando: ")
        if command == "aggiungi":
            shop.add_product()
        elif command == "elenca":
            shop.show_list()
        elif command == "vendita":
            shop.buy()
            shop.checkout()
        elif command == "profitti":
            shop.show_profit()
        elif command == "chiudi":
            shop.close()
            break
        elif command == "aiuto":
            shop.menu()
        else:
            print("Comando non valido.")
            shop.menu()
            continue    


if __name__ == "__main__":
    main()