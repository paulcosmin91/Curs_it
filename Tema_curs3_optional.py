#16 Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
# Declara o Lista cu 5 jucatori
#Schimbari_efectuate = va jucati voi cu valori diferite
#Schimbari_max = 3
echipa=['pele','maradona','hagi','zidane','ronaldo']
nume_jucator_schimbat=input('Numele jucatorului este:')
nume_jucator_intrat=input('Numele jucatorului este:')
schimbari_efectuate=int(input('Introdu un numar intre 0 si 3:'))
#Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
if nume_jucator_schimbat in echipa:
    if 0<schimbari_efectuate<=3:
       echipa.remove(nume_jucator_schimbat)
       echipa.append(nume_jucator_intrat)
       print('A iesit', nume_jucator_schimbat, 'a intrat', nume_jucator_intrat, 'mai aveti', schimbari_efectuate-1, 'schimbari.' )
    else:
        print('Nu se poate efectua schimbarea deoarece nu mai aveti schimbari.')
else:
    print('Nu se poate efectua schimbarea deoarece', nume_jucator_schimbat, ' nu este in teren.Mai aveti',schimbari_efectuate,'schimbari.')






