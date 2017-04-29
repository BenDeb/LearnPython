#!/usr/bin/python3

def table_multi(nb, max = 10):

    i = 1

    while i <= max:
        print(nb, " * ", i, " = ", nb * i)
        i += 1



if __name__ == "__main__":
    table_multi(14)
    table_multi(9)
    table_multi(10)
