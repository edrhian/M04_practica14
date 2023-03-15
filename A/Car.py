'''
Atributs de car
marca, color, cavalls, pais
'''
class Car:
    def __init__(self, brand, color, horsePower, country):
        self.brand = brand
        self.color = color
        self.horsePower = horsePower
        self.country = country

    #getters i setters
    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getHorsePower(self):
        return self.horsePower

    def setHorsePower(self, horsePower):
        self.horsePower = horsePower

    def getCountry(self):
        return self.country

    def setCountry(self, country):
        self.country = country

    #missatge
    def salutacio(self):
        print("La marca del cotxe és {brand}".format(brand = self.brand))
        print("El color del cotxe és {color}".format(color=self.color))
        print("Els cavalls del cotxe són {horsePower}".format(horsePower = self.horsePower))
        print("El cotxe és de {country}".format(country = self.country))

    #Objecte a diccionari
    def to_dict(self):
        return {
            "brand":self.brand,
            "color":self.color,
            "horse power":self.horsePower,
            "country":self.country
        }

