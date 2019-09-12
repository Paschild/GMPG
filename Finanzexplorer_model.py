import csv
from collections import OrderedDict

RECHNUNGSTYP = ""
superkategorien = []

# Define colours
WHITE = "#ffffff"

dct_Kategorien = {}
dct_Posten = {}
dct_categorierelations = OrderedDict()
dct_Schemata = OrderedDict()
dct_cells = {}


class Konzept:
    def __init__(self, name, color):
        self.rechnungstyp = RECHNUNGSTYP
        self.name = name
        self.color = color

        self.cells = []     # not the real cell_objects, just the position as (row, col)

    def __str__(self):
        return self.name


class Cell:
    def __init__(self, cellrow, cellcol, value, jahr):  # value = (<obj> kategorie, "--..", <obj> (ober)kategorie)
        self.row = cellrow
        self.col = cellcol
        self.value = value
        self.active = False

        self.jahr = jahr
        self.posten = dct_Posten[(self.value[0].id, self.jahr)]

        self.color = WHITE
        self.konzept = None

        self.zwischensumme = False
        self.oberkategorie = self.value[2]
        self.unterkategorien = []
        for s in dct_Schemata.values():
            if s.jahr == self.jahr:
                for c in s.cells:
                    if self.oberkategorie:
                        if self.oberkategorie.id == c.value[0].id:
                            c.unterkategorien.append(self)
                            c.zwischensumme = True

    def calculate_zwischensumme(self):
        if self.zwischensumme and self.posten.geldbetrag == 0:
            for k in self.unterkategorien:
                self.posten.geldbetrag += k.posten.geldbetrag

    def get_pos(self):
        return self.row, self.col


class KategorieRelation:
    def __init__(self, lst):
        self.id = int(lst[0])
        self.origin_id = int(lst[1])
        self.skos_typ = lst[2]
        self.target_id = int(lst[3])
        self.schema_id = int(lst[4])
        self.order_in_schema = lst[5]

        self.origin_kategorie = dct_Kategorien[self.origin_id]
        self.target_kategorie = dct_Kategorien[self.target_id]


class Kategorie:
    def __init__(self, lst):
        self.id = int(lst[0])
        self.bezeichnung = lst[1]
        self.spezifizierung = lst[2]
        self.hoere_oberkategorie = lst[3]

    def get_id(self):
        return self.id


class Schema:
    def __init__(self, lst):
        self.id = int(lst[0])
        self.bezeichnung = lst[1]

        self.typ = lst[1].split("_")[1]
        self.jahr = int(lst[1].split("_")[2][:4])

        self.KategorieRelationen = []  # list of obj(KategorieRelation)

        self.kategorien_hierarchisch = []

        for r in dct_categorierelations.values():
            if r.schema_id == self.id:
                self.KategorieRelationen.append(r)

        self.cells = set()


class Posten:
    def __init__(self, lst):
        self.kategorie_id = int(lst[0])
        self.rechnungskategorie = lst[1]
        # self.jahr_id = int(lst[2])
        self.jahr = int(lst[3])
        self.id = int(lst[4])
        if lst[5] in [None, 'None', '', ' ']:
            self.geldbetrag = 0.00
        else:
            self.geldbetrag = float(lst[5])


def import_csv(filename, sep=","):
    with open(filename + ".csv", newline='', encoding="utf-8-sig") as f1:
        filelist = list(csv.reader(f1, delimiter=sep))
        result = []
        for it in filelist:
            result.append(it)
        return result[1:]


def import_kategorien():
    global dct_Kategorien
    for x in import_csv("../Finanzexplorer-Git-data/Finanz_ID-Kategorie"):          # http://gmpg-intern.mpiwg-berlin.mpg.de:8888/explorer/549/
        dct_Kategorien[int(x[0])] = Kategorie(x)


def import_posten():
    global dct_Posten
    for x in import_csv("../Finanzexplorer-Git-data/Finanz_Posten-Jahr-Betrag"):   # http://gmpg-intern.mpiwg-berlin.mpg.de:8888/explorer/525/
        dct_Posten[(int(x[0]), int(x[3]))] = Posten(x)  # dict_key: (Kat_id, year)


def import_kategorierelations():
    global dct_categorierelations
    lst_categorierelations = []
    for x in import_csv("../Finanzexplorer-Git-data/Finanz_Kategorie_Relation"):   # http://gmpg-intern.mpiwg-berlin.mpg.de:8888/explorer/526/
        if x[5]:
            x[5] = int(x[5].split(".")[0])
        else:
            x[5] = 0
        lst_categorierelations.append(KategorieRelation(x))
    lst_categorierelations.sort(key=lambda kat: kat.order_in_schema)
    for y in lst_categorierelations:
        dct_categorierelations[int(y.id)] = y
    lst_categorierelations.clear()


def import_schemata():
    global dct_Schemata
    for x in import_csv("../Finanzexplorer-Git-data/Finanz_ID-Schema"):             # http://gmpg-intern.mpiwg-berlin.mpg.de:8888/explorer/548/
        # um nur die Daten zu laden, die auch dem gewählten Rechnungstypen entsprechen
        if x[1].split("_")[1] == RECHNUNGSTYP:
            dct_Schemata[int(x[0])] = Schema(x)


def get_dct_kategorien():
    return dct_Kategorien


def get_dct_posten():
    return dct_Posten


def get_dct_categorierelations():
    return dct_categorierelations


def get_dct_schemata():
    return dct_Schemata


def get_dct_cells():
    return dct_cells


def populate_cells():
    col = -1
    for year in range(1948, 2006):
        for schema in dct_Schemata.values():
            if schema.jahr == year:
                row = 0
                col += 1

                myView.frame.myGrid.SetColLabelValue(col, str(schema.jahr))
                for kategorie_in_Hierarchie in schema.kategorien_hierarchisch:
                    row += 1
                    temp = Cell(row, col, kategorie_in_Hierarchie, schema.jahr)
                    dct_cells[(row, col)] = temp
                    dct_Schemata[schema.id].cells.add(temp)
