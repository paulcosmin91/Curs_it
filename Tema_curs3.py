#1 Declara o lista note_muzicale in care sa pui do re mi etc pana la do
note_muzicale=['do','re','mi','fa','sol','la','si','do']
# a)Afiseaz-o
print('Lista mea este:', note_muzicale)
# b)Inverseaza ordinea folosind slicing si suprascrie aceasta lista
note_muzicale=note_muzicale[::-1]
# c)Printeaza varianta actuala (inversata)
print('Lista mea inversata este :' ,note_muzicale)
# d)Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (functia reverse)
note_muzicale.reverse()
# e)Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
print('Lista mea reinversata este:',note_muzicale)
#2 De cate ori apare ‘do’? (folosim functia count)
print('Nota do apare de : ',note_muzicale.count('do'), 'ori.')

#3 Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
lista1=[3,1,0,2]
lista2=[6,5,4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
#varianta 1 (concatenare)
lista3=lista1+lista2
print('Lista unita este :',lista3)
#varianta 2 (folosind extend)
lista1.extend(lista2)
print('Lista unita este:',lista1)

#4 Sortati si afisati lista generata la ex anterior (functia sort)
lista3.sort()
print('Lista sortata este:',lista3)
#Stergeti numarul 0 folosind o functie(functia remove)
lista3.remove(0)
#Afisati iar lista
print('Lista mea este:', lista3)

#5 Folosind un if verificati lista generata la ex3 si afisati
if len(lista3)>=1:
    print('Lista nu este goala.')
else:
    print('Lista este goala.')

#6 Folositi o functie care sa stearga lista de la ex3(functia del)
#del lista3[0::]
# functia del daca nu ii dau parametri sterge definitiv lista si apare ca nedeclarata
del lista3[0::]
#folosim functia clear
lista3.clear()
print(lista3)
#7 Copy paste la ex 5. Verificati inca o data.
if len(lista3)>=1:
    print('Lista nu este goala.')
else:
    print('Lista este goala.')

#8 Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1={'Ana':8,'Gigel':10,'Dorel':5}
# Folositi o functie ca sa afisati Elevii (cheile) (functia keys)
print(dict1.keys())

#9 Printati cei 3 elevi si notele lor
print('Ana a luat nota',dict1['Ana'])
print('Gigel a luat nota', dict1['Gigel'])
print('Dorel a luat nota', dict1['Dorel'])

#10  Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6 (suprascriere)
dict1['Dorel']=6
# Printati nota dupa modificare
print('Nota lui Dorel dupa contestatie este:', dict1['Dorel'])

#11 Gigel se transfera din clasa
# Cautati o functie care sa il stearga (functia pop)
dict1.pop('Gigel')
print(dict1)
# Vine un coleg nou. Adaugati Ionica, cu nota 9
dict1['Ionica']=9
#Printati noii elevi
print(dict1)

#12 Set zile_sapt =  , 'sambata', 'duminica'}
zile_sapt={'marti','miercuri','joi','vineri','sambata','duminica'}
weekend={'sambata','duminica'}
#adaugati in zile_sapt, 'luni'
zile_sapt.add('luni')
# afisati zile_sapt
print(zile_sapt)

#13 folositi un if pentru a verifica daca weekend est un subset al zile_sapt
# (folosim issubset)
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zile_sapt.')
else:
    print('Weekend nu este un subset al zile sapt.')
# folosind valorile din setul weekend
if ('sambata' and 'duminica') in zile_sapt:
    print('Weekend este un subset al zile_sapt.')
else:
    print('Weekend nu este un subset al zile sapt.')

#14 Afisati diferentele dintre aceste 2 seturi
#diferenta
print(zile_sapt-weekend)
# functia symmetric_difference
print(zile_sapt.symmetric_difference(weekend))

#15 Afisati intersectia elementelor din aceste 2 seturi
# folosind &
print(zile_sapt&weekend)
#folosind intersection
print(zile_sapt.intersection(weekend))














if(x=='Lastun'):
         masini_vechi.append('Lastun')