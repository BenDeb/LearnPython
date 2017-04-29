#!/usr/bin/python3


nb = input(" nb ")
nb2 = input(" nb2 ")

try:
    nb = int(nb)
    nb2 = int(nb2)
    resultat = nb / nb2
except ZeroDivisionError:
    print("division par zéro!")
except TypeError:
    print("erreur de type")
except NameError:
    print("variable non définie")
except ValueError:
    print("value error")
else:
    print("le résultat est", resultat)
finally:
    print(nb, nb2)

i = 1
assert i == 1
assert i == 2
