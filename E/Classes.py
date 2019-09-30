class Auto():

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

class Auto():

    def __init__(self, color, ano):
        self.color = color
        self.ano = ano



    def get_info(self):
        print("El auto es " + self.color + " y de " + self.ano)

toyota = Auto("rojo", "1995")
toyota.get_info()

audi = Auto("negro", "2005")
audi.get_info()





class Cliente():

    def __init__ (self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def get_name(self):
        print(self.nombre + " " + self.apellido)

maria = Cliente("Maria", "Perez")
maria.get_name()

jose = Cliente("Jose", "Martinez")
jose.get_name()





class Suma:
    primer_num = 0
    segundo_num = 0
    resultado = 0

    def __init__(self, p, s):
        self.primer_num = p
        self.segundo_num = s

    def display(self):
        print ("Primer numero = " + str(self.primer_num))
        print ("Segundo numero = " + str(self.segundo_num))
        print ("Resultado = " + str(self.resultado))

    def calculo(self):
        self.resultado = self.primer_num + self.segundo_num

num_uno = Suma(1, 2)
num_uno.calculo()
num_uno.display()


num_dos = Suma(3, 4)
num_dos.calculo()
num_dos.display()'''



class Autor:
    def __init__(self, nombre, genero, ano):
        self.nombre = nombre
        self.genero = genero
        self.ano = ano

    def incremento_ano(self):
        self.ano = self.ano + 1

    def display(self):
        print ("Este autor se llama " + self.nombre + ", escribia " + self.genero + " y nacio en " + str(self.ano))

borges = Autor("Borges", "ficcion", 1899)
borges.display()

octavio = Autor("Octavio", "ensayos", 1914)
octavio.display()

#Clase con Constructor, cada vez que un objeto se cree en la clase, se acitva esta funcion. Las variables seran definidad por el argumento del objeto.
