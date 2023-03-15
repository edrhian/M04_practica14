"""Els atributs de la classe book són:
 el nom, la cobertura, els numeros de pagina, l'autor, la data de publicaió i el preu"""
class book:
    def __init__(self, name, cover, npage, author, date, price):
        self.name = name
        self.cover = cover
        self.npage = npage
        self.author = author
        self.date = date
        self.price = price

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getCover(self):
        return self.cover
    def setCover(self, cover):
        self.cover = cover
    def getNpage(self):
        return self.npage
    def setNpage(self, npage):
        self.npage = npage
    def getAuthor(self):
        return self.author
    def setAuthor(self, author):
        self.author = author
    def getDate(self):
        return self.date
    def setDate(self, date):
        self.date = date
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
#Text que surt per pantalla
    def info(self):
        print("El llibre és diu {name}".format(name=self.name))
        print("La cobertura és de material {cover}".format(cover=self.cover))
        print("El llibre té {npage} pàgines".format(npage=self.npage))
        print("L'autor es diu {author}".format(author=self.author))
        print("És va publicar el {date}".format(date=self.date))
        print("El preu és de {price} €".format(price=self.price))
#Retorna un diccionari
    def to_dict(self):
        return{
            "name":self.name,
            "cover":self.cover,
            "npage":self.npage,
            "author":self.author,
            "date":self.date,
            "price":self.price
        }