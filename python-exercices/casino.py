#!/usr/bin/python3

numero = input("entrez un numéro \n")
try:
    numero = int(numero)
    assert numero >= 0
    assert numero <= 50
except AssertionError:
    print("le numéro doit se trouver entre 0 et 50 inclus! ")
