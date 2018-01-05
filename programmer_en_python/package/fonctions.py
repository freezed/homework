#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# fonctions.py : essai d'utilisation d'un package

# OpenClassrooms - Apprenez à programmer en Python - Modularité
# https://openclassroom/courses/apprenez-a-programmer-en-python/pas-a-pas-vers-la-modularite-2-2

"""Module de test, contient les fonctions crees durant le cours
OpenClassrooms - Apprenez à programmer en Python"""

def table(n, m=11):
    """Chapitre 1.7 - Modularite
    Affiche la table de multiplication d'un nombre
    de 1 * n
    a m * n """
    for i in range(1, m):
        print(i,"x",n,"=",i * n)

# test de _table_
if __name__ == "__main__":
    table(3)

def afficher_flottant(flot):

    """Chapitre 2.3 - Entre chaînes et listes
    Affiche un nombre a virgule flottante tronque a 3 decimales
    et remplace le point (.) par une virgule (,)"""

    string = str(flot)
    splited_string = string.split('.')
    entier = splited_string[0]

    if len(splited_string[1]) <= 3:
        decimal = splited_string[1][:len(splited_string[1])]
    else:
        decimal = splited_string[1][:3]

    flotant_formate =  ','.join((entier,decimal))
    print(flotant_formate)

if __name__ == "__main__":
    afficher_flottant(1.123456789)
    afficher_flottant(1.12)
    afficher_flottant(0.12)
