# 11 Verifica daca x are minim 4 cifre (x e int)
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x=int(input('Numarul x este :'))
if(len(str(x))>=4):
    print('x are minimum 4 caractere')
else:
    print('x nu are minimum 4 caractere')

#12 Verifica daca x are exact 6 cifre
if(len(str(x))==6):
    print('x are 6 caractere')
else:
    print('x nu are 6 caractere')

#13 Verifica daca x este numar par sau impar (x e int)
if(x%2==0):
    print('x este numar par.')
else:
    print('x este numar impar.')

#14 x, y, z (int)
#Afiseaza care este cel mai mare dintre ele?
x=int(input('Numarul x este :'))
y=int(input('Numarul y este :'))
z=int(input('Numarul z este :'))
if(x>y and x>z):
    print(x)
if(y>x and y>z):
    print(y)
if (z>x and z>y):
    print(z)
# se poate folosit functia max
print(max(x,y,z))

#15 X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
if(x>0 and y>0 and z>0 and x+y+z==180):
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid')

#16 Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
a='Coral is either the stupidest animal or the smartest rock'
x=int(input('Numarul x este: '))
print(a[0:-x])

#17 acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5
b= a[0:5] + a[len(a)-5::]
print(b)

#18 acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
#(hint: este o functie care te ajuta sa faci asta)
#folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '
index=a.index('rock')
print(index)
print(a[0:index])

#19 citeste de la tastatura un string
# verifica daca primul si ultimul caracter sunt la fel
# se va folosi un assert
# atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat
a=input('Stringul este: ')
assert(a[0].casefold()==a[len(a)-1].casefold())
print ( a + ' este acceptat.')

#20 avand stringul '0123456789'
# afisati doar numerele pare
# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)
a='0123456789'
if int(a[0])%2==0:
    print(a[0])
    pass
if int(a[1])%2==0:
    print(a[1])
    pass
if int(a[2])%2==0:
    print(a[2])
    pass
if int(a[3])%2==0:
    print(a[3])
    pass
if int(a[4])%2==0:
    print(a[4])
    pass
if int(a[5])%2==0:
    print(a[5])
    pass
if int(a[6])%2==0:
    print(a[6])
    pass
if int(a[7])%2==0:
    print(a[7])
    pass
if int(a[8])%2==0:
    print(a[8])
    pass
if int(a[9])%2==0:
    print(a[9])
    pass
# pentru numerele impare este exact la fel doar difera condiitia
if int(a[0])%2==1:
    print(a[0])
    pass
if int(a[1])%2==1:
    print(a[1])
    pass
if int(a[2])%2==1:
    print(a[2])
    pass
if int(a[3])%2==1:
    print(a[3])
    pass
if int(a[4])%2==1:
    print(a[4])
    pass
if int(a[5])%2==1:
    print(a[5])
    pass
if int(a[6])%2==1:
    print(a[6])
    pass
if int(a[7])%2==1:
    print(a[7])
    pass
if int(a[8])%2==1:
    print(a[8])
    pass
if int(a[9])%2==1:
    print(a[9])
    pass
