#!/usr/bin/python3

def table(nb, max = 9):
    i = 0
    while i < max:
        print(nb, " * ", (i + 1), " = ", nb * (i + 1))
        i += 1
if __name__ == "__main__":
    table(7)
