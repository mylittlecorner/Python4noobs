#!/usr/bin/env python3

import random

lista= list()
ksawery_p=27

for i in range(5):
    rand = random.randint(27,200)
    lista.append(rand-ksawery_p)

print(lista)
