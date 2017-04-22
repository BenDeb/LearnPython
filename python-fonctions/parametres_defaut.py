#!/usr/bin/python3
# Il est possible de définir des paramètres par défaut dans une fonction. ces derniers sont utilisés si l'utilisateur ne rentre aucun paramètre. Cela n'empêche pas l'utilisateur d'entrer des paramètres différents des paramètres par défaut.



def fonction_defaut(a=5, b=10):
    print(a, " + ", b, " = ", a + b)

#fonction_defaut()
#5 + 10 = 15

#fonction_defaut(10,20)
#10 + 20 = 30
fonction_defaut(7,8)
7  +  8  =  15
    
#En définissant une fonction du meme nom, on écrase la fonction précédente : 

def fonction_defaut(a=5, b=10):
    print(a, " * ", b, " = ", a * b)

fonction_defaut(7,8)
7  *  8  =  56
