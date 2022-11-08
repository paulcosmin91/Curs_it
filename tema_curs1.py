#1 in cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# variabila = o cutiuta de valori(date) situata intr-o portiune de memorie

#2 Declarati si initializati cate o variabila din urmatoarele tipuri
#string
nume='Popescu'
#int
varsta=24
#float
inaltime=1.78
#boolean
casatorit=True

#3 Utilizati functia type pentru a verifica daca au tipul de date asteptat
print(type(nume))
print(type(varsta))
print(type(inaltime))
print(type(casatorit))

#4 Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila
#suprascriere
#verificati tipul acesteia
print(round(inaltime))
inaltime=2
print(type(inaltime))

#5 folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
#(rezolvati nepotrivirile de tip prin ce modalitate doriti)
print(f'Ma numesc {nume} si am {varsta} de ani.')
print('Ma numesc ' + nume + ' si am inaltimea de '+ str(inaltime) + ' cm.')
print(f'Ma numesc {nume}, am inaltimea de {inaltime} si sunt casatorit. ')
print('Ma numesc ' + nume + ', am ' + str(varsta) + ' de ani' +', am inaltimea de ' + str(inaltime) + ' cm si sunt casatorit.')

#6 citeste de la tastatura numele
#citeste de la tastatura prenumele
#afiseaza 'Numele complet are x caractere'
nume=input('Numele este ')
prenume=input('Prenumele este ')
x= len(nume+prenume)
print('Numele complet are ' +str(x) + ' caractere.' )

#7 citeste de la tastatura lungimea
#citeste de la tastatura latimea
#afiseaza 'Aria dreptunghiului este x'
lungime=int(input('Lungimea dreptunghiului este '))
latime=int(input('Latimea dreptunghiului este ' ))
x=lungime*latime
print('Aria dreptunghiului este ' + str(x) + ' .')

#8  Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
#afisati de cate ori apare cuvantul 'the'
my_str=('Coral is either the stupidiest animal or the smartest rock')
x= my_str.count(' the ')
print('Cuvantul the apare de: ', x )

#9 Acelasi string
#inlocuieste the cu THE peste tot
#printeaza rezultatul
x=my_str.replace(' the ' , ' THE ')
print(x)

#10 acelasi string
#folositi un assert ca sa verificati daca acest string contine doar numerere
a='Coral is either the stupidiest animal or the smartest rock'
assert(a.isnumeric())



