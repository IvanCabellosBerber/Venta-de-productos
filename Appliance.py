class Appliance:
    def __init__(self, name, type, manufacturer, unity_price, quantity, last_day_registry):
        self.applianceName = name
        self.applianceType = type
        self.manufacturer = manufacturer
        self.unityPrice = unity_price
        self.quantity = quantity
        self.lastDayRegistry = last_day_registry

    def register_product(self):
        file = open("stock.dat", "a")
        file.write(
            str(self.applianceName) +
            "," + str(self.applianceType) +
            "," + str(self.manufacturer) +
            "," + str(self.unityPrice) +
            "," + str(self.quantity) +
            "," + str(self.lastDayRegistry + "\n")
        )
        file.close()
