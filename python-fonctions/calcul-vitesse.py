#!/usr/bin/python3
#1. Affectez les variables temps et distance par les valeurs 6.892 et 19.7. Calculez et affichez la valeur de la vitesse.
# Améliorez l’affichage en imposant un chiffre après le point décimal.
distance = float(input("entrez la distance"))
temps = float(input("entrez le temps"))

vitesse = (distance / temps)
print(round(vitesse, 1))
