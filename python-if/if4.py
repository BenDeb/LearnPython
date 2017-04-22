nom = ' ' 

print("nom?")
nom = input()
if nom == "benjamin":
    print("quel age as-tu", nom)
    age = input()
    if age < 30:
        print("jeune")
    else:
        print("encore jeune!")
elif nom == "thao":
    print("bonjour", nom,", quel animal aimes-tu?")
    animal = input()
    if animal == "chien":
        print("wooof")
    elif animal == "chat":
        print("miaou")
else:
    print("je ne te connais pas")
