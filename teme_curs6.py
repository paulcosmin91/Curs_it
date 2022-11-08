#1 Clasa Cerc
class Cerc:
    pi=3.14159265
# constructor
    def __init__(self,raza,culoare):
        self.raza=raza
        self.culoare=culoare
#metode
    def descrie_cerc(self):
        print('Cercul are raza de ',self.raza, 'cm si are culoarea ', self.culoare)
    def aria(self):
        return float(self.pi)*int(self.raza)**2
    def diametru(self):
        return 2*int(self.raza)
    def circumferinta(self):
        return 2*float(self.pi)*int(self.raza)
#obiecte
cerc1=Cerc('5','albastru')
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

cerc2=Cerc('10','galben')
cerc2.descrie_cerc()
print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())

#2 Clasa dreptunghi
class Dreptunghi:
# constructor
    def __init__(self,lungime,latime,culoare):
        self.lungime=lungime
        self.latime=latime
        self.culoare=culoare
# metode
    def descrie(self):
        print('Dreptunghiul are lungimea de ',self.lungime,'cm, are latimea de ', self.latime, 'cm si are culoarea', self.culoare)
    def aria(self):
        return int(self.lungime)*int(self.latime)
    def perimetrul(self):
        return 2*int(self.lungime)+2*int(self.latime)
    def schimba_culoarea(self,noua_culoare):
        self.culoare=noua_culoare
#obiecte
dreptunghi1=Dreptunghi('10','5','verde')
dreptunghi1.descrie()
print(dreptunghi1.aria())
print(dreptunghi1.perimetrul())
dreptunghi1.schimba_culoarea('visiniu')
dreptunghi1.descrie()

dreptunghi2=Dreptunghi('12','8','gri')
dreptunghi2.descrie()
print(dreptunghi2.aria())
print(dreptunghi2.perimetrul())
dreptunghi2.schimba_culoarea('violet')
dreptunghi2.descrie()

#3 Clasa Angajat
class Angajat:
#constructor
     def __init__(self,nume,prenume,salariu):
         self.nume=nume
         self.prenume=prenume
         self.salariu=salariu
#metode
     def descrie(self):
         print(f'Ma numesc',self.nume,self.prenume, 'si am salariu de', self.salariu,'RON.')
     def nume_complet(self):
         return self.nume +' '+ self.prenume
     def salariu_lunar(self):
         return int(self.salariu)
     def salariu_anual(self):
         return int(self.salariu)*12
     def marire_salariu(self,procent):
         return int(self.salariu)+(int(self.salariu)*procent/100)
angajat1=Angajat('Popescu','Aurel','4000')
angajat1.descrie()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(angajat1.marire_salariu(10))

angajat2=Angajat('Popescu','Maria','3500')
angajat2.descrie()
print(angajat2.nume_complet())
print(angajat2.salariu_lunar())
print(angajat2.salariu_anual())
print(angajat2.marire_salariu(10))

#4 Clasa Cont
class Cont:
# constructor
    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold
#metode
    def afisare_sold(self):
        print('Titularul',  self.titular_cont,' are in contul', self.iban, 'suma de:', self.sold,' lei.')
    def debitare_cont(self,suma):
        if self.sold>=suma:
           self.sold = int(self.sold) - int(suma)
           return self.sold
        else:
           return 'Suma nu paote fi debitata! Introduceti o suma mai mica!'
    def creditare_cont(self,suma):
        self.sold=int(self.sold)+int(suma)
        return self.sold
cont1=Cont('RO41RON001','Popescu Octavian','10000')
cont1.afisare_sold()
print(cont1.debitare_cont('11000'))
print(cont1.creditare_cont('7000'))

cont2=Cont('RO41RON002','Popescu Maria','23000')
cont2.afisare_sold()
print(cont2.debitare_cont('11000'))
print(cont2.creditare_cont('7000'))

