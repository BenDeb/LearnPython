#!/usr/bin/python3

from random import randrange
from math import ceil

argent = 1000
continuer = True

while continuer == True:
    numero = -1
    while numero < 0 or numero > 49:
        numero = input("Entrez le numéro sur lequel vous souhaitez miser\n")
        try:
            numero = int(numero)
        except TypeError:
            print("Veuillez entrer un nombre\n")
        except ValueError:
            print("Veuillez entrer un nombre\n")
        if numero < 0 or numero > 49:
            print("veuillez entrer un numéro entre 0 et 49 inclus, merci!")
    print("vous avez choisi le numéro", numero)
    mise = 0
    while mise > argent or mise <= 0:
        mise = input("entrez le montant que vous souhaitez miser\n")
        try:
            mise = int(mise)
        except TypeError:
            print("Vous devez entrer un nombre")
        except ValueError:
            print("Veuillez entrer un nombre")
        if mise > argent:
            print("vous n'avez pas assez d'argent pour miser une telle somme!")
    print("Très bien! Vous avez misé", mise, " euros sur le numéro ", numero, " ! ")
    print("La roue s'apprête à tourner!")
    case = randrange(50)
    print("La bille s'arrête sur la case", case, " ! ")
    if numero == case:
        print("Jackpot! Votre mise est multipliée par 3! ")
        mise += ceil(mise * 3)
        argent += mise
    if numero % 2 == case % 2:
        print("Pas mal, votre mise est multipliée par 1.5")
        mise += ceil(mise * 0.5)
        argent += mise
    else:
        print("Dommage, vous perdez votre mise...")
        argent -= mise
    print("vous disposez de", argent, " euros")
    if argent <= 0:
        print("vous avez perdu, vous n'avez plus d'argent")
        continuer = False
    else:
        quit = input("Voulez-vous quitter?")
        if quit == "oui" or quit == "o" or quit == "yes" or quit == "y":
            continuer = False
