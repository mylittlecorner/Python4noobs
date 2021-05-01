#!/usr/bin/env python3
import random
lista=list()
for i in range(10):
    value=random.randint(17,76)
    lista.append(value)

print(lista)
print(lista[::3])
print(lista[-3:])
print(lista[-5:])
print(lista[3:6])
