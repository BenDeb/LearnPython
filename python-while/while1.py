nombre = 0
while nombre != 5:
    print('cherchez le nombre magique')
    nombre = input()
    if int(nombre) < 5:
        print('plus grand!')
        continue
    if int(nombre) > 5:
        print('plus petit!')
        continue
    if int(nombre) == 5:
        break
print('bravo ben')

