#11 citeste de la tastatura un string de dimensiune impara
#afiseaza caracterul din mijloc
echipa=input('Numele eschipei este ')
assert(len(echipa)%2==1)
c=round(len(echipa)//2)
print(echipa[c])

#12 Folosind assert, verificati daca un string este palindrom
a='radar'
assert(a[0::]==a[::-1])
print(a + ' este palindrom')

#13 folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
#si salveaza fiecare cuvant intr-o variabila
#acum printeaza ambele variabile pentru verificare
a=input('Stringul este ')
x,y=a.split()
print(a)
print(x,y)

#14 citeste un string de la tastatura (eg: alabala portocala)
#salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
#capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
a=input('Stringul este ')
x=a[0]
y=a[1:-1]
z=x.upper()
c=y.replace(x,z)
print(c)

#15 citeste un user de la tastatura
#citeste o parola
#afiseaza: 'Parola pt user x este ***** si are x caractere'
user=input('User-ul este : ')
parola=input('Parola este : ')
a=int(len(user))
b=int(len(parola))
c='*' * b
print('Parola pentru user-ul ' + user + ' este ' + str(c)  + ' si are ' + str(b) + ' caractere.')









