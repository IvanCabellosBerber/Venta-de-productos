from Appliance import Appliance
from datetime import date


def add_product():
    print("You need to enter some information to the new product")
    name = str(input("Name of the product: "))
    type = str(input("Type of the product: "))
    manufacturer = str(input("Manufacturer of the product: "))
    unity_price = str(input("Unitary price of the product: "))
    quantity = str(input("Inital stock of the product: "))
    new_appliance = Appliance(name, type, manufacturer, unity_price, quantity, date.today())
    new_appliance.register_product()


def modify_product():
    with open("stock.dat") as pds:
        line = pds.readline()
        while line:
            print(line.split(","))
            line = pds.readline()
    res = str(input("Tell me the number of the product to modify"))
    with open("stock.dat", "r") as f:
        lines = f.readlines()
    with open("stock.dat", "w"):
        for line in lines:
            if line.__contains__(res):
                name = str(input("New name: "))
                type = str(input("New type: "))
                manufacturer = str(input("New manufacturer: "))
                unity_price = str(input("New unitary price: "))
                quantity = str(input("New stock: "))
                new_appliance = Appliance(name, type, manufacturer, unity_price, quantity, date.today())
                new_appliance.register_product()
                #cacaaaaaaaaa

def modify_stock():
    return None


def sell_product():
    return None


def delete_product():
    with open("stock.dat") as pds:
        line = pds.readline()
        while line:
            print(line.split(","))
            line = pds.readline()
    res = str(input("Tell me the number of the product to delete"))
    with open("stock.dat", "r") as f:
        lines = f.readlines()
    with open("stock.dat", "w") as f:
        for line in lines:
            if not line.__contains__(res):
                f.write(line)


def show_products():
    with open("stock.dat") as pds:
        line = pds.readline()
        while line:
            print(line)#rrrrrrrrrrrr
            line = pds.readline()


class Main:
    def print_menu(self):
        print("\n      Welcome to Drassil")
        print(" Your Home Appliances Store APP")
        print("================================")
        print("'                              '")
        print("' 1. Add a new product         '")
        print("' 2. Modify product            '")
        print("' 3. Modify stock product      '")
        print("' 4. Delete a product          '")
        print("' 5. Show all products results '")
        print("' 6. Sell product              '")
        print("' 0. EXIT                      '")
        print("'                              '")
        print("================================\n")

    def start_app(self):
        self.print_menu()
        res = str(input("What do you want to do"))
        while res != "0":
            if res == "1":
                add_product()
            elif res == "2":
                modify_product()
            elif res == "3":
                modify_stock()
            elif res == "4":
                delete_product()
            elif res == "5":
                show_products()
            elif res == "6":
                sell_product()
            else:
                print("CHOICE A NUMBER FROM DE MENU")
            self.print_menu()
            res = str(input("Do you want to do another think"))


main = Main()
main.start_app()
