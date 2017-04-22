#!/usr/bin/python3


""" Fonction : Rentrer deux nombres, le premier (nb) est le nombre à multiplier, le deuxième (max) est le nombre maximum par lequel sera multiplié nb
# Exemple : 
#>>> table(6, 14)
1  *  6  =  6
2  *  6  =  12
3  *  6  =  18
4  *  6  =  24
5  *  6  =  30
6  *  6  =  36
7  *  6  =  42
8  *  6  =  48
9  *  6  =  54
10  *  6  =  60
11  *  6  =  66
12  *  6  =  72
13  *  6  =  78
14  *  6  =  84"""

def table(nb, max):
    i = 0
    while i < max:
        print((i + 1), " * ", nb, " = ", (i + 1) * nb)
        i += 1
