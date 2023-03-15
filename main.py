import json

from A.Car import Car
from A.school import school

cars = [
    Car("Toyota", "blanc", 120, "Japo"),
    Car("Nissan", "blau", 180, "Alemanya"),
    Car("Wolkswagen", "vermell", 80, "Alemanya"),
    Car("Peugeot", "gris", 160, "Espanya"),
    Car("Mini", "groc", 60, "Francia")
]

schools = [
    school("Escola del treball", 6, 100, 1000, 2, 6),
    school("Escola del bricolatge", 5, 90, 800, 1, 7),
    school("Escola carlot", 3, 40, 600, 1, 7),
    school("Escola pia", 1, 10, 100, 4, 6),
    school("Escola espol", 2, 20, 200, 3, 8)
]


cars_list = [c.to_dict() for c in cars]
schools_list = [s.to_dict() for s in schools]

#Objecte contenidor
data = {"cars":cars_list, "schools":schools_list}

#Guardar objecte contenidor
with open("json_API/a.json", "w") as file:
    json.dump(data, file)
