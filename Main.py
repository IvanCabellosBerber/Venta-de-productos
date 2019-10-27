from random import randint
from Appliance import Appliance
from datetime import date

"""
Creamos una lista statica, que esta será la que se dedique a guardar y después modificar los productos. Trabajaremos con la lista
que esta es la que luego refleje los productos en los ficheros, así será mucho más fácil todo.
"""
products: list = []


class Main:
    """
    La clase Main se encargará de llamar a todas las funciones staticas para administrar el programa. Tendra un menú y
    una impresion de este. Según el resultado del menú este llamará a una función o otra.
    """

    def print_menu(self):
        print("\n      Welcome to Drassil")
        print(" Your Home Appliances Store APP")
        print("================================")
        print("'                              '")
        print("' 1. Sell product              '")
        print("' 2. Show all products results '")
        print("' 3. Add a new product         '")
        print("' 4. Modify stock product      '")
        print("' 5. Delete a product          '")
        print("' 0. EXIT                      '")
        print("'                              '")
        print("================================\n")

    def start_app(self):
        """
        Funciones a las que llamaremos
        """
        self.print_menu()
        res = str(input("What do you want to do"))
        while res != "0":
            if res == "1":
                sell_product()
            elif res == "2":
                show_products("stock.dat")
            elif res == "3":
                add_product()
            elif res == "4":
                modify_product()
            elif res == "5":
                delete_product()
            else:
                print("CHOICE A NUMBER FROM DE MENU")
            self.print_menu()
            res = str(input("Do you want to do another think"))


def rewrite_appliances(products: list):
    """
    Esta función es la que se encará de reescribir los cambios en el fichero de los productos.
    """
    open("stock.dat", 'w').truncate()
    for product in products:
        write_appliance(product)


def write_appliance(product: Appliance):
    """
    Lo usaremos para escribir un producto en concreto
    """
    try:
        with open("stock.dat", 'a') as file:
            file.write(
                product.applianceName + "," +
                product.applianceType + "," +
                product.manufacturer + "," +
                str(product.unityPrice) + "," +
                str(product.quantity) + "," +
                str(product.lastDayRegistry)
            )
    except():
        print("SOMETHING WRONG WRITING NEW PRODUCT")
        main.start_app()


def register_products(file: str):
    """
    Esta función sirve para registrar los productos del fichero a la aplicación, guardará los productos dentro de la
    lista.
    """
    try:
        with open(file, 'r') as p:
            line: str = p.readline()
            if line.startswith('['):
                line = p.readline()
            while line:
                newAppliance = Appliance(line)
                products.append(newAppliance)
                line = p.readline()
        for pds in products:
            print(pds.__str__())
        p.close()
    except():
        print("ERROR DURING REGISTERING PRODUCTS")
        main.start_app()


def sell_product():
    """
    Esta función como indica será para vender un producto en concreto
    """
    show_products("stock.dat")
    name_product = str(input("Name of the product: "))

    for pds in products:
        if pds.applianceName.__contains__(name_product):
            print(pds)
            # Preguntamos al usuario si esta seguro que es ese producto el que quiere vender
            res = str(input("Is this product that you want to sell? y/n"))
            if res.__contains__("y"):
                try:
                    unity = int(input("How many unities you want to sell"))
                    # Aquí hará una comprobación del stock del producto y volverá a pedir al usuario un stock más
                    # correcto
                    while pds.quantity < unity and pds.quantity - unity < 0:
                        print("We doesn't have stock enough")
                        unity = int(input("How many unities you want to sell"))
                    # Restamos al stock las unidades pedidas
                    pds.quantity -= unity
                    # Y si el stock es menos de 5 saltará un aviso al usuario para que pida más stock
                    if pds.quantity <= 5:
                        print(pds.applianceName, " has ", pds.quantity, " stock right now, please contact to providers")
                    make_a_bill(pds, unity)
                except:
                    print("ERROR DURING SELLING PRODUCT")
                    main.start_app()
    rewrite_appliances(products)


def show_products(file: str):
    """
    Función solo para mostrar los productos al usuario
    """
    try:
        with open(file, 'r') as p:
            line: str = p.readline()
            if line.startswith('['):
                line = p.readline()
            while line:
                line = p.readline()
        for pds in products:
            print(pds.__str__())
        p.close()
    except:
        print("ERROR DURING SHOWING PRODUCTS")
        main.start_app()


def add_product():
    """
    Añadir un producto nuevo a la lista
    """
    try:
        print("REGISTER NEW PRODUCT")
        producto: str = ""
        producto += str(input("Name: "))
        producto += str(input("Type: "))
        producto += str(input("Manufacturer: "))
        producto += str(input("Stock: "))
        producto += str(input("Price: "))
        producto += str(date.today())
        newProduct = Appliance(producto)
        products.append(newProduct)
        rewrite_appliances(products)
    except:
        print("ERROR DURING ADDING PRODUCT")
        main.start_app()


def modify_product():
    """
    Esta función se encará de modificar un producto y sobreescribirlo.
    """
    show_products("stock.dat")
    name_product = str(input("What do you want to modify?"))
    for pds in products:
        if name_product.__contains__(pds.applianceName):
            print(pds)
            # Como antes, diremos al usuario si este es el producto que quiere modificar
            res = str(input("Is this product that you want to sell? y/n"))
            if res.__contains__("y"):
                # Le diremos que quiere modificar y posteriormente sobreescriremos los valores
                print("Name\n"
                      "Type\n"
                      "Manufacturer\n"
                      "Stock\n"
                      "Price\n")
                res = str(input("What do you want to modify?")).upper()
                if res.startswith("NAME"):
                    res = str(input("New name: "))
                    pds.applianceName = res
                if res.startswith("TYPE"):
                    pds.applianceType = str(input("New type: "))
                if res.startswith("MANUFACTURE"):
                    pds.manufacturer = str(input("New manufacturer: "))
                if res.startswith("STOCK"):
                    pds.quantity = int(input("New stock: "))
                if res.startswith("PRICE"):
                    pds.unityPrice = int(input("New price: "))
    rewrite_appliances(products)


def delete_product():
    """
    Función para eliminar un producto de la lista, y después sobreescribiremos.
    """
    show_products("stock.dat")
    name_product = str(input("Name of the product to DELETE: "))

    for pds in products:
        if pds.applianceName.__contains__(name_product):
            print(pds)
            res = str(input("Is this product that you want to DELETE? y/n"))
            if res.__contains__("y"):
                res = str(input("DELETE? y/n"))
                if res.__contains__("y"):
                    try:
                        products.pop(pds)
                    except:
                        print("ERROR DURING SELLING PRODUCT")
                        main.start_app()
    rewrite_appliances(products)


def make_a_bill(product: Appliance, quantity):
    """
    Con esta función haremos una factura, que será el resultado de un PDF, pediremos al usuario el nombre del cliente y
    registraremos la compra. Mostrando el producto, precio unitario y el total de este.
    """
    costumer = str(input("Name of the costumer: "))
    bill_num = str(randint(10000, 90000))
    bill = open(costumer + bill_num + str(date.today()) + ".pdf", "a")
    bill.write(
        "Date: " + str(date.today()) + "\n" +
        "Num: " + bill_num + "\n" +
        "Name: " + costumer + "\n" +
        "===============================" + "\n" +
        "Product: " + product.applianceName + "\n" +
        "Unity price: " + str(product.unityPrice) + ", TOTAL: " + str(product.unityPrice * quantity)
    )
    bill.close()


##############################
# INICIALIZAR LA APLICACIÓN
main = Main()
register_products("stock.dat")
main.start_app()
##############################
