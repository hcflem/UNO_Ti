from random import *
from time import *
from ti_system import *
disp_clr()
valeurs = ['0','1','2','3','4','5','6','7','8','9']
couleurs = ['bleu','rouge','jaune','verte']
bonus=['+2','<~>','skip','+4']
deck=[]
while len(deck)<40:
    i=0
    while i!=75:
        val=randint(0,9)
        coul=randint(0,3)
        bonu=randint(0,3)
        luck=randint(0,3)
        if [valeurs[val],couleurs[coul]] not in deck:
            deck.append([valeurs[val],couleurs[coul]])
        if luck==0:
            if [bonus[bonu]] not in deck:
                if bonus[bonu]=='+2':
                    deck.append([bonus[bonu],couleurs[coul]])
                else:
                    deck.append([bonus[bonu]])
        elif luck==1:
            if [bonus[bonu]] not in deck:
                if bonus[bonu]=='+4':
                    deck.append(['8', 'verte'])
                elif bonus[bonu]=='+2':
                    deck.append([bonus[bonu],couleurs[coul]])
                else:
                    deck.append([bonus[bonu]])
        else:
            val2=randint(0,9)
            coul2=randint(0,3)
            bonu2=randint(0,3)
            if [valeurs[val2],couleurs[coul2]] not in deck:
                deck.append([valeurs[val2],couleurs[coul2]])
        i+=1

main=[]
for i in range(7):
    main.append(deck.pop(i))
    
def pioche():
    if len(main)>6:
        return "Main pleine!"
    main.append(deck.pop())
    return main

def jouer(a):
    x=int(input("Donnez le numéro de la carte que vous souhaitez jouer :\n      "))
    x-=1
    main.pop(x)
a=0
print("      _____\n     | Uno |\n      -----")
sleep(2)
while a!=99:
    print("\n  1- Jouer\n  2- Piocher\n 99- Fin de game\n")
    print(main)
    a=int(input("Que souhaitez-vous faire ? \n      "))
    if a==1:    
        if len(main)==1:
            a=99
            print("Bravo !")
        else:
            jouer(a)
    elif a==2:
        pioche()
        
    