# 5 Clasa Factura
from datetime import datetime
from tabulate import tabulate


class Factura():
    seria = 'FPP'

    # constructor
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_buc

    # metode
    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        return cantitate_noua

    def schimba_pretul(self, pret):
        self.pret_bucata = pret
        return pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return nume

    def genereaza_factura(self):
        print('Factura seria', self.seria, 'numar', self.numar)
        print('Data:', datetime.now())
        pret_total = int(self.pret_bucata) * int(self.cantitate)
        head = (["Produs", "Cantitate", "pret bucata", "Total"])
        data = ([self.nume_produs, self.cantitate, self.pret_bucata, str(pret_total)], [])
        print(tabulate(data, head))


factura1 = Factura('001', 'carne', '100', '25')
print(factura1.schimba_cantitatea('40'))
print(factura1.schimba_pretul('100'))
print(factura1.schimba_nume_produs('faina'))
print('__________________________')
factura1.genereaza_factura()


# 6 Clasa Masina
class Masina:
    culoare = 'gri'
    viteza_actuala = 0
    culori_disponibile = {'rosu', 'albastru', 'verde', 'negru', 'galben'}
    marca = 'Audi'
    inmatriculata = False

    # constructor
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    # metode
    def descrie(self):
        head = (["Marca", "Model", "Viteza_actuiala", "Viteza_maxima", "Culoare", "Inmatriculata"])
        data = ([self.marca, self.model, self.viteza_actuala, self.viteza_maxima, self.culoare, self.inmatriculata], [])
        print(tabulate(data, head))

    def inmatriculare(self):
        self.inmatriculata = True
        print(self.inmatriculata)

    def vopseste(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare = culoare_noua
            print(self.culoare)
        else:
            print('Eroare')

    def accelereaza(self, viteza):
        self.viteza_actuala = viteza
        if int(viteza) < 0:
            print('Eroare')
        elif int(viteza) > int(self.viteza_maxima):
            self.viteza_actuala = self.viteza_maxima
            print(self.viteza_actuala)
        else:
            int(self.viteza_actuala) == int(viteza)
            print(self.viteza_actuala)

    def franare(self):
        self.viteza_actuala = 0
        print(self.viteza_actuala)
masina1 = Masina('80', '200')
masina1.descrie()
print('_______________')
masina1.inmatriculare()
masina1.vopseste('galben')
masina1.accelereaza('100')
print('_____________')
masina1.descrie()
masina1.franare()

# 7 Clasa TodoList
class TodoList:
    dict()
# metode
    def adauga_task(self,nume,descriere):
        self.dict= {nume: descriere}
        print(self.dict)
    def finalizare_task(self,nume):
        self.dict.pop(nume)
        print(self.dict)
    def afiseaza_todo_list(self):
        print(list(self.dict.keys()))
    def afiseaza_detalii_suplimentare(self,nume_task):
        if nume_task not in self.dict.keys():
           x=input('Vrei sa introducem task-ul?True or False:')
           if x=='True':
              self.dict[nume_task]=input('Detaliile task-ului sunt:')
              print(self.dict)
           if x=='False':
              print('La revedere!')
        else:
            print('Task_ul este deja in todo_list.')
todo_list1=TodoList()
todo_list1.adauga_task('Curatenie','Trebuie sa duci gunoiul')
todo_list1.finalizare_task('Curatenie')
todo_list1.afiseaza_todo_list()
todo_list1.afiseaza_detalii_suplimentare('Calatorie')







