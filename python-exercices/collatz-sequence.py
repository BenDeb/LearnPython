#!/usr/bin/python3

def collatz(number):
    reste = number % 2
    if reste == 0:
        return (number // 2)
    else:
        return (3 * number + 1)

try:
    nombre_choisi = int(input("Entrez un entier:\n"))
except ValueError:
    print("il faut un entier!\n")
r = collatz(nombre_choisi)
print(r)
while r != 1:
    r = collatz(r)
    print(r)
