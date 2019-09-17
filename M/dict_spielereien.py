from collections import defaultdict

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.name = {(self.row, self.column): list_posten[x].value}
        self.inhalt = self.name[self.row, self.column]


class Posten:
    def __init__(self, value):
        self.value = value


list_posten = []
list_posten.append(Posten("Hallo"))
list_posten.append(Posten("Hola"))
list_posten.append(Posten("Ciao"))

dict = {}
dict2 = {(0, 1): 0, (1, 2): 1, (2, 3): 2}
dict3 = {}
list = []
dict_list = []
y = 1
z = 10


for x in range (0, 3):
    dict[x, y] = z
    list.append(Cell(x, y))
    y = y + 1
    z = z * 2


for k in list:
    print(k.row, k.column, k.name[k.row, k.column])
    print(k.name)
    print(k.inhalt)
    dict_list.append(k.name)

print("----------")
print(dict)
for k, v in dict.items():
    print(k)
    print(v)

print("----------")
print(dict_list)
print(dict_list[0][0, 1])


print("uuuuuuuuuuuu")
print(dict2)
print(dict2.items())