import json

from A.Car import Car
from A.school import school
from B.cat import cat
from B.book import book

#Llista amb objectes car
cars = [
    Car("Toyota", "blanc", 120, "Japo"),
    Car("Nissan", "blau", 180, "Alemanya"),
    Car("Wolkswagen", "vermell", 80, "Alemanya"),
    Car("Peugeot", "gris", 160, "Espanya"),
    Car("Mini", "groc", 60, "Francia")
]
#Llista amb objectes school
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


#Crear una llista per a la classe cat amb els seus valors
books = [
    book("El laberinto", "dur", 300, "Marcos", "11-11-2011", 20),
    book("Shadow", "dur", 878, "Mark", "20-11-2015", 15),
    book("El rio", "dur", 278, "Juan", "27-11-2008", 30),
    book("El espejo", "dur", 118, "Jordi", "11-10-2018", 25),
    book("Cien años de soledad", "dur", 438, "Gabriel", "22-11-2007", 10)
]
#Crear una llista per a la classe book amb els seus valors
cats = [
    cat("Abisinio", 5, "blanc", 2),
    cat("Bengala", 8, "blanc", 4),
    cat("Rizo amenricano", 4, "blanc", 2),
    cat("Bengala", 9, "blanc", 4),
    cat("Birmano", 12, "blanc", 5)
]
#Convertir les instàncies cat i book en una llista de diccionari JSON
cats_list = [c.to_dict() for c in cats]
books_list = [b.to_dict() for b in books]
#Envolvem la llista dins d'un contenedor
data = {"books":books_list, "cats":cats_list}
#Guardar el contenidor en un arxiu anomenat a.json
with open("json_API/b.json", 'w') as file:
    json.dump(data, file)