#!/usr/bin/python3

print("multiples de 2 : entrez un nombre pour savoir si c'est un multiple de 2")

sortir = ''
nb = int(input())
while sortir != "oui":
    if nb % 2 == 0:
        print("multiple de 2")
    else:
        print("non multiple de 2")
    print("voulez-vous sortir? oui/non")
    sortir = input()
    
print("aurevoir")
