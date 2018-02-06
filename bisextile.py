#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cours OC/python 3 - Les structures conditionnelles
[Ex 1.4: Bisextile](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-structures-conditionnelles#/id/r-231173)

Déterminer si une année saisie par l'utilisateur est bissextile
"""

annee = input("Saisir une année:")
annee = int(annee)

if (annee % 400) == 0 :
    print(annee," est bisextile (divisible par 400)")
elif (annee % 4) == 0 and (annee % 100) != 0:
    print(annee," est bisextile (divisible par 4, mais pas par 100)")
else:
    print(annee," n'est PAS bisextile.")
liste = []

# La suite ne fait pas parti du TP: bonus perso

print("Voici la liste des annees bisextiles entre 1900 & 2030 :")

for a in range(1900,2030):
    if ((a % 400) == 0) or ((a % 4) == 0 and (a % 100) != 0):
        liste.append(a)

print(liste)
