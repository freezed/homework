#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.5-continue.py : remplacer while/continue par une structure plus claire

# OpenClassrooms - Apprenez à programmer en Python - Les boucles
# https://openclassroom

print("   Fonctionnement a reproduire:")
i = 1
while i < 20:
    if i % 3 == 0:
        i += 4
        print("On incremente i de 4. i =", i)
        continue
    print("La variable i =", i)
    i += 1

print("   boucle «for», probleme de scope avec la valeur de i")
for i in range(1,20):
    if i % 3 == 0:
        i += 4
        print("On incremente i de 4. i = ", i)
    else:
        print("La variable i =", i)
        i += 1

print("   Remplacement du «contine» par un «else»:")
i = 1
while i < 20:
    if i % 3 == 0:
        i += 4
        print("On incremente i de 4. i =", i)
    else:
        print("La variable i =", i)
        i += 1
