#11. Functie care primeste o luna din an si returneaza cate zile are acea luna
from calendar import monthrange
def zile_luna (year,month):
    return monthrange(year,month)[1]
x=zile_luna(2022,5)
print('Luna selectata are',x, 'zile.')

#12. Functie calculator care sa returneze 4 valori
#Suma, diferenta, inmultirea, impartirea a 2 numere
def calculator(x,y):
    sum=x+y
    dif=x-y
    mul=x*y
    div=x/y
    return sum,dif,mul,div
a,b,c,d=calculator(10,5)
print('Suma numerelor este,',a)
print('Diferenta numerelor este :',b)
print('Rezultatul inmultirii numerelor este:',c)
print('Rezultatul impartirii numerelor este',d)

#13 Functie care primeste o lista de cifre (adica doar 0-9)
# returneaza de cate ori apare fiecare cifra in lista
def count_numbers(list):
   dict= {}
   for i in range (10):
        dict[i]=list.count(i)
   return dict
x=count_numbers([1,2,3,4,5,1,9,7,2,0,3,5,5,0,7,6,2,1])
print('Fiecare cifra apare in felul urmator:',x)

#14 Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        val_max = a
    elif (b >= a) and (b >= c):
        val_max = b
    else:
        val_max = c
    return val_max
x=maximum(10,10,8)
print('Valoarea maxima dintre cele 3 numere este:', x)

#15 Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
def suma_numerelor(n):
    s=sum(range(1,n+1))
    return s
x=suma_numerelor(10)
print('Suma numerelor este:', x)





