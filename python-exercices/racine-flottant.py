#!/usr/bin/python3
#Saisissez un flottant. S’il est positif ou nul, affichez sa racine, sinon affichez un message d’erreur.

from math import sqrt
flottant = float(input("entrez un flottant "))

if flottant >= 0:
	print(round(sqrt(flottant), 2))
else:
	print("erreur, vous avez entré un nombre négatif!")
	
