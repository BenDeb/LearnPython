#!/usr/bin/python3

import random
def table_multi(nb, max = 10):
    i = 0
    while i < max:
        print((i + 1), " * ", nb, " = ", (i + 1) * nb)
        i += 1


nb = random.randint(1, 10)
multi = table_multi(nb)
