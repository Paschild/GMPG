import wx
import wx.grid
from collections import defaultdict

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.name = {(self.row, self.column): list_posten[x].value}


class Posten:
    def __init__(self, value):
        self.value = value


list_posten = []
list_posten.append(Posten("Hallo"))
list_posten.append(Posten("Hola"))
list_posten.append(Posten("Ciao"))

dict = {}
dict2 = {(0, 1): 0, (1, 2): 1, (2, 3): 2}
list = []
y = 1
z = 10

for x in range (0, 3):
    dict[x, y] = z
    list.append(Cell(x, y))
    y = y + 1
    z = z * 2




print(list)

for k in list:
    print(k.row, k.column, k.name[k.row, k.column])

print(dict)