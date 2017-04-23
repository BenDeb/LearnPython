#!/usr/bin/python3

import random

def pair_impair(a):
    print(a)
    if a % 2 == 0:
        return("pair")
    else:
        return("impair")

a = random.randint(1, 1000)
resultat = pair_impair(a)
print(resultat)
