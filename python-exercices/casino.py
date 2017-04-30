#!/usr/bin/python3


import random
from math import ceil
continuer = True
argent = int(input("combien d'argent avez-vous? \n"))
while continuer = True
    while numero < 0 and numero > 49:
        numero = input("entrez un numéro \n")
        try:
            numero = int(numero)
        except TypeError:
            print("Vous n'avez pas entré un nombre!")
        if numero < 0:
            print("Entrez un nombre égal ou supérieur à 0!")
        if numero < 49:
            print("Entrez un numéro inférieur à 50!")

    mise = input("quelle somme souhaitez-vous miser? \n")
    if mise > argent:
        print("impossible, vous n'avez pas assez d'argent")
        continue
    case = random.randrange(50)
    print("la bille est tombée sur la case", case)
    if case == numero:
        mise *= 4
        ceil(mise)
        print("La chance vous sourit, la bille tombe sur la case", case)
        argent = argent + mise
    elif (case % 2 == 0 and numero % 2 == 0) or (case % 2 != 0 and numero % 2 != 0):
#On multiplie la mise par 0.5 et on l'arrondit la mise au chiffre supérieur
        mise = ceil(mise * 0.5)

        print(mise, "2")
        argent += mise
    else:
        print(mise, "3")
        ceil(mise)
        argent = argent - mise
    print("il vous reste", argent)
    ceil(argent)
    continuer = input("souhaitez-vous continuer? oui/non \n")
if argent <= 0:
    print("vous avez perdu, vous n'avez plus d'argent!")
