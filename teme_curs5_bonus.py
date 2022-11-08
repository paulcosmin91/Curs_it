#16 Functie care primesete 2 liste de numere (numerele pot fi dublate)
#Returnati numerele comune
def nr_comune(a,b):
    c=set(a).intersection(b)
    return c
x=nr_comune([1,2,3,4,5,8,9],[9,4,6,7,0,5,3])
print('Numerele comune celor 2 liste sunt:',x)

#17 Functie care sa aplice o reducere de pret
def discount(pret,reducere):
    dis=reducere*pret/100
    if pret>dis:
        pret=pret-dis
        return pret
    else:
        return 'Reducerea e invalida.'
x=discount(1000,20)
print('Pretul dupa reducere este :', x)

#18 Functie care sa afiseze data si ora curenta din ro
# cu datetime.now
from datetime import datetime
def data_ora_crt():
    now=datetime.now()
    return now
x=data_ora_crt()
print('Data si ora curenta in Romania este:', x)
# cu pytz folosind timezone
from datetime import datetime
import pytz
def data_ora_crt(a):
    IST=pytz.timezone(a)
    now=datetime.now(IST)
    return now
x=data_ora_crt('Europe/Bucharest')
y=data_ora_crt('Asia/Shanghai')
print('Data si ora curenta in Romania este:',x)
print('Data si ora curenta in China este:',y)

#19 Functie care sa afiseze cate zile mai sunt pana la ziua ta  sau pana la craciun
from datetime import date
def days_rem(date_a,date_b):
    delta_time=date_a-date_b
    return delta_time.days
x=days_rem(date(2022,12,25),date(2022,10,23))
print('Pana la Craciun mai sunt:',x,'zile.')









