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
        print(i, "x", n, "=", i * n)


def afficher_flottant(flot):

    """Chapitre 2.3 - Entre chaînes et listes
    Affiche un nombre a virgule flottante tronque a 3 decimales
    et remplace le point (.) par une virgule (,)"""

    if type(flot) is not float:
        print("Le parametre doit etre de type float!")
    else:
        flot = str(flot)
        entier, decimal = flot.split('.')
        print(
            ','.join((entier, decimal[:3]))
        )


def affiche(*liste_parametres, sep=' ', fin='\n'):

    """Chapitre 2.3 - Entre chaînes et listes:
    Fonction chargée de reproduire le comportement de print.
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés.
    On doit passer à print une unique chaîne, en lui spécifiant de
    ne rien mettre à la fin : print(chaine, end='')"""

    contenu = str()
    for parametre in liste_parametres:
        contenu += str(parametre)
        contenu += sep

    contenu = contenu + fin
    print(contenu, end='')


if __name__ == "__main__":
    # Tests de la fonction 'affiche'
    affiche("'string'", "'autre string; 1'", 2)
    affiche(1.12, "'string'", "'autre string; 1'", 2)
    affiche(False, True, 1.12, "'string'", "'autre string; 1'", 2)

    # Tests de la fonction 'afficher_flottant'
    #afficher_flottant(1.123456789)
    #afficher_flottant(1.12)
    #afficher_flottant(0.1)
    #afficher_flottant("a")
    #afficher_flottant(False)
    #afficher_flottant(100)

    # test de la fonction 'table'
    #table(3)
