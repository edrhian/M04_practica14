'''
Atributs de school
Nom, numero de pisos, numero de aules, area, numero de ascensors, numero de assignatures
'''
class school:
    def __init__(self, sName, nFloors, nClassrooms, area, nElevators, nSubjects):
        self.sName = sName
        self.nFloors = nFloors
        self.nClassrooms = nClassrooms
        self.area = area
        self.nElevators = nElevators
        self.nSubjects = nSubjects

    # getters i setters
    def getsName(self):
        return self.sName

    def setsName(self, sName):
        self.sName = sName

    def getNFloors(self):
        return self.nFloors

    def setNFloors(self, nFloors):
        self.nFloors = nFloors

    def getNClassrooms(self):
        return self.nClassrooms

    def setNClassrooms(self, nClassrooms):
        self.nClassrooms = nClassrooms

    def getArea(self):
        return self.area

    def setArea(self, area):
        self.area = area

    def getNElevators(self):
        return self.nElevators

    def setNElevators(self, nElevators):
        self.nElevators = nElevators

    def getNSubjects(self):
        return self.nSubjects

    def setNSubjects(self, nSubjects):
        self.nSubjects = nSubjects
    #Missatge
    def info(self):
        print("El nom de l'escola és {sName}".format(sName=self.sName))
        print("L'escola té {nFloors} pisos".format(nFloors=self.nFloors))
        print("L'escola té {nClassrooms} aules".format(nClassrooms=self.nClassrooms))
        print("L'escola té una area de {area} metres quadrats".format(area=self.area))
        print("L'escola té {nElevators} ascensors".format(nElevators=self.nElevators))
        print("L'escola ofereix {nSubjects} assignatures".format(nSubjects=self.nSubjects))

    #Objecte a diccionari
    def to_dict(self):
        return {
            "name":self.sName,
            "floors":self.nFloors,
            "classrooms":self.nClassrooms,
            "area":self.area,
            "elevators":self.nElevators,
            "subjects":self.nSubjects
        }