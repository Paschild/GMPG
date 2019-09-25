'''class Auto():

    def get_info(self):
        print("El auto es " + self.color + " y de " + self.ano)




toyota = Auto()
toyota.color = "rojo"
toyota.ano = "1995"
toyota.get_info()


audi = Auto()
audi.color = "negro"
audi.ano = "2001"
audi.get_info() '''     #Clase con atributos y función




#Clases con Constructor(__init__):

'''class Auto():

    def __init__(self, color, ano):
        self.color = color
        self.ano = ano



    def get_info(self):
        print("El auto es " + self.color + " y de " + self.ano)

toyota = Auto("rojo", "1995")
toyota.get_info()

audi = Auto("negro", "2005")
audi.get_info()'''





'''class Cliente():

    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def get_name(self):
        print(self.nombre + " " + self.apellido)

maria = Cliente("Maria", "Perez")
maria.get_name()

jose = Cliente("Jose", "Martinez")
jose.get_name()'''