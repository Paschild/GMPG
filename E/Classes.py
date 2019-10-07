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





class Autor:

    especie = "humanos"


    def __init__(self, nombre, genero, ano):
        self.nombre = nombre
        self.genero = genero
        self.ano = ano

    def display(self):
        print ("Este autor se llama " + self.nombre + ", escribia " + self.genero + " y nacio en " + str(self.ano))

borges = Autor("Borges", "ficcion", 1899)
borges.display()

octavio = Autor("Octavio", "ensayos", 1914)
octavio.display()

cortazar = Autor("Cortazar", "ficcion", "1914")
cortazar.display()



class Periodista(Autor):
    def politica(self, politica):
        self.politica = politica
        print(self.nombre + " tenia una opinion de " + self.politica)


gabo = Periodista("Gabo", "ficcion", 1930)
gabo.politica("izquierda")



class Diplomatico(Autor):
    def matrimonio(self, matrimonio):
        self.matrimonio = matrimonio
        print(self.nombre + " " + self.matrimonio + " estaba casado.")


fuentes = Diplomatico("Fuentes", "ambos", "1920")
fuentes.matrimonio("si")


class Trabajo:

    autores = []

    def __init__(self,autores):
        self.autores = autores



mis_autores = [
    Periodista("Gabo", "ficcion", 1930),
    Diplomatico("Fuentes", "ambos", "1920")
]

trabajos_ = Trabajo(mis_autores)


print("Hay autores de {} trabajos.".format(len(trabajos_.autores)))
for autor in trabajos_.autores:
    print(autor.nombre + " escribe " + autor.genero + " y nacio en " + str(autor.ano))

print("Y ambos son {}".format(autor.especie))




class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    is_hungry = True

    def eat(self):


    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))
