#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# fonction.py : fonctions du fichier pendu.py

""" Rassemble les fonctions du script pendu.py """


def check_letter(letter, target):
    """
        Verifie la presence de **letter** dans **target**
        Retourne la liste des positions de la letter ou False
        @letter str
        @target list of letters
    """
    if len(letter) != 1 or len(target) < 2 and letter is not str:
        return False

    else:
        return [k for k, v in enumerate(target) if letter == v]


def cls():
    """ Efface l'historique de la console """
    import os
    os.system('clear')
    return


def stringalise (letter_list):
    """
        Convertit un liste en une chaine
        @letter_list list()
        @return string()
    """
    stringalised = str()
    for letter in letter_list:
        stringalised = stringalised + ' ' + letter

    return stringalised


if __name__ == "__main__":
    # Tests de la fonction
    print(check_letter('A', ['M', 'A', 'M', 'O', 'U', 'T', 'H']))
    print(check_letter('M', ['M', 'A', 'M', 'O', 'U', 'T', 'H']))
    print(check_letter('o', ['M', 'A', 'M', 'O', 'U', 'T', 'H']))
    print(check_letter('À', ['M', 'A', 'M', 'O', 'U', 'T', 'H']))
    print(check_letter(1, ['M', 'A', 'M', 'O', 'U', 'T', 'H']))
    print(check_letter(False, ['M', 'A', 'M', 'O', 'U', 'T', 'H']))
