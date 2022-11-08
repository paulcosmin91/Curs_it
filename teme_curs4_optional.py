# 11
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for x in range(len(alte_numere)):
    if alte_numere[x]%2==0:
        numere_pare.append(alte_numere[x])
    else:
        numere_impare.append(alte_numere[x])
    if alte_numere[x]>0:
        numere_pozitive.append(alte_numere[x])
    else :
        numere_negative.append(alte_numere[x])
print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

#12
for x in range(len(alte_numere)):
    for y in range(x+1, len(alte_numere)):
        if alte_numere[x]>alte_numere[y]:
            alte_numere[x],alte_numere[y]=alte_numere[y],alte_numere[x]
print(alte_numere)

#13
import random
numar_secret=random.randint(1,30)
numar_ghiciri=0
while numar_ghiciri<5:
    numar=int(input('Numarul este:'))
    numar_ghiciri+=1
    if numar<numar_secret:
        print('Nr ghicit e mai mic.')
    if numar>numar_secret:
        print('Nr ghicit e mai mare.')
        break
if numar==numar_secret:
        print('Felicitari.Ai ghicit numarul'+ str(numar_ghiciri)+ ' ghiciri')
else:
         print('Nu ai ghicit numarul. Numarul secret este :' , numar_secret)

#14
randuri= int(input('Numarul introdus de la tastatura este : '))
for i in range (randuri+1):
    for j in range (i):
        print(i, end='')
    print('')

#15
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for x in tastatura_telefon:
    for y in x:
        print('Cifra curenta este',y)



