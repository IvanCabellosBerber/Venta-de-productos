from datetime import date


class Appliance:
    def __init__(self, string):
        str_splited = string.split(",")
        self.applianceName: str = str_splited[0]
        self.applianceType: str = str_splited[1]
        self.manufacturer: str = str_splited[2]
        self.unityPrice: int = int(str_splited[3])
        self.quantity: int = int(str_splited[4])
        self.lastDayRegistry: date = str_splited[5]

    def __str__(self):
        return str(
            "[" + self.applianceName + "] " +
            "[" + self.applianceType + "] " +
            "[" + self.manufacturer + "] " +
            "[" + str(self.unityPrice) + "] ")
