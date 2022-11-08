#1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# if else functioneaza in felul urmator:
# pasul 1: se verifica o conditie pentru a realiza o anumita actiune
# pasul 2: daca conditia este indeplinita se executa acea actiune
# pasul 3 : daca conditia nu este indeplinita atunci se executa alta actiune

#2 Verifica si afiseaza daca x este numar natural sau nu
x=int(input('Numarul x este '))
if(x>0):
    print('X este numar natural.')
else :
    print('x nu este numar natural.')

#3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
if(x>0):
    print('X este numar pozitiv.')
elif (x==0):
    print('x este numar neutru.')
else :
    print('x nu este numar negativ.')

#4 Verifica si afiseaza daca x este intre -2 si 13
if(-2<x<13):
  print('x este intre -2 si 13.')
else:
  print('x nu este intre -2 si 13.')
#5 Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x=int(input('Numarul x este : '))
y=int(input('Numarul y este : '))
print(x-y)
if((x-y)<5):
  print('Diferenta dintre x si y este mai mica decat 5.')
elif((x-y)==5):
  print('Diferenta dintre x si y este egala cu 5.')
else:
  print ('Diferenta dintre x si y este mai mare decat 5.')

#6 Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
if not(5<x<27):
   print(' x nu este intre 5 si 27.')
else :
   print('x este intre 5 si 27.')

# 7 x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
if(x==y):
  print(' x este egal cu y.')
elif(x>y):
    print('x este mai mare ca y.')
else:
  print('y este mai mare ca x.')

#8 X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
x=int(input('Numarul x este : '))
y=int(input('Numarul y este : '))
z=int(input('Numarul z este : '))
if(x==y==z):
    print('Triunghiul este exchilateral.')
elif((x==y) or (x==z) or (y==z)):
   print('Triunghiule este isoscel.')
else:
   print('Triunghiul este oarecare.')

#9 Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu
a=input('Litera citita este :')
if a.lower () in ('a','e','i','o','u'):
 print('Litera citita este o vocala.')
elif a.upper() in ('A','E','I','O','U'):
 print('Litera citita este o vocala.')
else:
 print('Litera citita este o consoana.')
# o alta varianta ar fi sa folosim de mai multe ori operatorul logic or

''' 10 Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
nota=int(input('Nota primita este: '))
if(nota>9):
  print('Ai primit nota A.')
elif(nota >8):
  print('Ai primit nota B.')
elif(nota >7):
  print('Ai primit nota C.')
elif(nota >6):
  print('Ai primit nota D.')
elif(nota >4):
  print('Ai primit nota E.')
else:
  print('Ai primit nota F.')
