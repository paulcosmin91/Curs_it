#21 Verificare imbarcare persoane
varsta=int(input('Am varsta de: '))
insotit_de_mama= input('Este insotit de mama? True/False:')
if insotit_de_mama.capitalize()=='True':
  print('Este insotit de mama. ')
elif insotit_de_mama.capitalize()=='False':
  print('Nu este insotit de mama.')
else:
  print('Introdu True sau False.')
insotit_de_tata= input('Este insotit de tata? True/Flase:')
if insotit_de_tata.capitalize()=='True':
  print('Este insotit de tata. ')
elif insotit_de_tata.capitalize()=='False':
  print('Nu este insotit de tata.')
else:
  print('Introdu True sau False.')
pasaport= input ('Are pasaport? True/False:')
if pasaport.capitalize()=='True':
  print('Are pasaport.')
elif pasaport.capitalize()=='False':
  print('Nu are pasaport.')
else:
  print('Introdu True sau False.')
act_permisiune_mama= input('Are act de permisiune de la mama? True/False:')
if act_permisiune_mama.capitalize()=='True':
  print('Are act de permisiune de la mama.')
elif  act_permisiune_mama.capitalize()=='False':
  print('Nu are act de permisiune de la mama.')
else:
  print('Introdu True sau False.')
act_permisiune_tata=input('Are act de permisiune de la tata? True/False:')
if act_permisiune_tata.capitalize()=='True':
  print('Are act de permisiune de la tata.')
elif  act_permisiune_tata.capitalize()=='False':
  print('Nu are act de permisiune de la tata.')
else:
  print('Introdu True sau False.')
if(varsta>=18 and pasaport.capitalize()=='True'):
    print('Are minim 18 ani si are pasaport.Se poate imbarca.')
elif (varsta>=18 and pasaport.capitalize()=='False'):
     print('Are minim 18 ani si nu are pasaport.Nu se poate imbarca')
elif(varsta<18 and pasaport.capitalize()=='False'):
    print('Nu are 18 ani, nu are pasaport. Nu se poate imbarca.')
elif(varsta<18 and pasaport.capitalize()=='True' and insotit_de_mama.capitalize()=='True' and insotit_de_tata.capitalize()=='True'):
    print('Nu are 18 ani, are pasaport si este insotit de ambii parinti. Se poate imbarca')
elif(varsta<18 and pasaport.capitalize()=='True' and insotit_de_mama.capitalize()=='False' and insotit_de_tata.capitalize()=='False'):
    print('Nu are 18 ani, are pasaport si nu este insotit de parinti. Nu se poate imbarca.')
elif(varsta<18 and pasaport.capitalize()=='True' and insotit_de_mama.capitalize()=='True' and act_permisiune_tata.capitalize()=='True'):
   print('Nu are 18 ani, este insotit de mama si are act de permisiune de la tata. Se poate imbarca. ')
elif(varsta<18 and pasaport.capitalize()=='True' and insotit_de_tata.capitalize()=='True' and act_permisiune_mama.capitalize()=='True'):
        print('Nu are 18 ani, este insotit de tata si are act de permisiune de la mama. Se poate imbarca.')
else:
    print('Nu se poate imbarca.')

#22 Joc ghicit zarul
import random
dice_roll=random.randint(1,6)
b=int(input('Numarul ghicit de utilizator este:'))
if(b<1 or b>6):
    print('Alege un numar de la 1 pana la 6.')
elif(b==dice_roll):
    print('Ai ghicit. Felicitari. Ai ales ' +str(b)+ 'si zarul a fost '+str(dice_roll)+ ' .' )
elif(b>dice_roll):
    print('Ai gresit.Ai ales un numar mai mare. Ai ales '+str(b)+ ' si a fost '+str(dice_roll)+' .')
else:
    print('Ai gresit.Ai ales un numar mai mic. Ai ales ' + str(b) + ' si a fost ' + str(dice_roll) + ' .')
