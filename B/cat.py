"""Els atributs de la classe cat són:
 la raça, el color, l'edat del gat i el seu pes"""
class cat:
    def __init__(self, race, color, age, weight ):
        self.race = race
        self.color = color
        self.age = age
        self.weight = weight

    def getRace(self):
        return self.race
    def setRace(self, race):
        self.race = race

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age

    def getWeight(self):
        return self.weight
    def setWeight(self, weight):
        self.weight = weight

# Text que surt per pantalla
    def info(self):
        print("La raza del gat és:  {race}".format(race=self.race))
        print("Té {age} anys".format(age=self.age))
        print("És de color: {color} ".format(color=self.color))
        print("Pesa {weight} kg".format(weight=self.weight))

# Retorna un diccionari
    def to_dict(self):
        return{
            "race":self.race,
            "age":self.age,
            "color":self.color,
            "weight":self.weight
        }

