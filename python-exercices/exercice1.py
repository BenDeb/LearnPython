#!/usr/bin/python3

quitter = ''
annee = 2017
while quitter != "y":
    age = int(input("Quel est votre age? "))
    annee100 = (2017 - age)  + 100
    print("en", annee100, " vous aurez 100 ans")
    quitter = input("voulez-vous quitter? y/n ")
