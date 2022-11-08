#1 Functie care sa calculeze si sa returneze suma a 2 numere
def suma(a,b):
     c=a+b
     return c
x=suma(4,5)
print('Suma numerelor este :', x)

#2 Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def par_impar(numar):
   if numar%2==0:
      return True
   else:
       return False
x= par_impar(4)
print('Valoarea afirmatiei este:',x)

#3 Functie care returneaza numarul total de caractere din numele tau complet.
def lungime (nume):
    x = len(nume)
    return x
y= lungime('Popescu Maria')
print('Numarul total de caractere este', y)
#fara a lua in calcul spatiile
def lungime (nume):
    x = sum(not chr.isspace() for chr in nume)
    return str(x)
y= lungime('Popescu Maria')
print('Numarul total de caractere fara spatii este:', y)

#4 Functie care returneaza aria dreptunghiului
def aria_dreptunghi(a,b):
    aria = a * b
    return aria
x=aria_dreptunghi(5,6)
print('Aria dreptunghiului este', x)

#5 Functie care returneaza aria cercului
import math
def aria_cerc(r):
    aria=math.pi*r*r
    return aria
x=aria_cerc(7)
print('Aria cercului este', x)

#6 Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
def chr_in_string(a,string):
    for i in range(len(string)):
        if a==string[i]:
          return True
        else :
          return False
x=chr_in_string('a','alfabet')
print('Valoarea afirmatiei este:',x)

#7 Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y
def my_function(string):
    x = 0
    y = 0
    for i in range(len(string)):
         if string[i].islower():
            x=x+1
         elif string[i].isupper():
            y=y+1
         else:
             pass
    print('Numarul de caractere lower case este:', x)
    print('Numarul de caractere upper case este :', y)
my_function('Alfa Beta Gama Delta43 ')

#8 Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def pozitiv(list):
    list_poz=[]
    for i in range(len(list)):
        if list[i]>=0:
            list_poz.append(list[i])
    return list_poz
x=pozitiv([-1,2,-9,3,-8,4,5,10])
print('Lista cu numere pozitive este:', x)

#9 Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA care dintre ele este mai mare
def comparare(x,y):
    if x>y:
       print('Primul numar',x, 'este mai mare decat al doilea numar', y)
    elif x<y :
        print('Al doilea numar', y, ' este mai mare decat primul numar', x)
    else:
        print('Numerele sunt egale')
comparare(10,15)

#10 Functie care primeste un numar si un set de numere.
def add_to_set(a,b):
    if a not in b:
        b.add(a)
        print('Am adaugat numarul ',a, 'in setul', b)
        return True
    else:
        print('Nu am adaugat numarul',a, 'in setul', b, '.Acesta exista deja.')
        return False
x=add_to_set(10,{1,5,6,7,8})
print('Valoarea afirmatiei este', x)



