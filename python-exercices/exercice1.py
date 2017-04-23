#!/usr/bin/python3

i = 0
quitter = ''
annee = 2017
while quitter != "y":
    age = int(input("Quel est votre age? "))
    annee100 = (2017 - age)  + 100
    print("en", annee100, " vous aurez 100 ans")
    nb = int(input("entrez un nombre"))
    while i < nb:
            print("en", annee100, " vous aurez 100 ans")
            i += 1
    quitter = input("voulez-vous quitter? y/n ")
    i = 0
