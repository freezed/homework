#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Author: freezed <git@freezed.me> 2018-01-17
    Licence: `GNU GPL v3`_
    Version: 0.1

    .. _GNU GPL v3: http://www.gnu.org/licenses/
"""


class TableauNoir:
    """
        Definis une surface sur laquelle on peut ecrire.

        On peut lire et effacer, par jeu de methodes. L'attribut
        modifie est 'surface'
    """

    def __init__(self):
        """Par defaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, texte):
        """
            Methode permettant d'ecrire sur la surface du tableau.

            Si la surface n'est pas vide, on saute une ligne avant de
            rajouter le message a ecrire

            :texte a: Le texte a ajouter au tableuu
            :type a: string
            :return: None
        """
        if self.surface != "":
            self.surface += "\n"
        self.surface += texte

    def lire(self):
        """
            Cette methode se charge d'afficher, grace a print,
            la surface du tableau
        """

        print(self.surface)

    def effacer(self):
        """Cette methode permet d'effacer la surface du tableau"""
        self.surface = ""


class Duree:
    """
        Classe contenant des durees sous la forme d'un nombre de minutes
        et de secondes
    """

    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min  # Nombre de minutes
        self.sec = sec  # Nombre de secondes

    def __str__(self):
        """Affichage MM:SS"""
        return "{:02}:{:02}".format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        """L'objet a ajouter est un entier, le nombre de secondes"""
        self.sec += objet_a_ajouter  # On ajoute la duree

        if self.sec >= 60:  # Si le nombre de secondes >= 60
            self.min += self.sec // 60
            self.sec = self.sec % 60

        return self  # On renvoie la nouvelle duree

    def __sub__(self, objet_a_soustraire):
        """
            Soustrait le nombre de seconde passe en parametre
            Ne retourne jamais de duree negative

            :param a: secondes a soustraire
            :type a: int
            :return: object
        """
        allsec = (self.min * 60) + self.sec

        if objet_a_soustraire > allsec:
            self.min = 0
            self.sec = 0
        else:
            allsec -= objet_a_soustraire  # On soustrait la duree
            self.min = allsec // 60
            self.sec = allsec % 60

        return self  # On renvoie la nouvelle duree


if __name__ == "__main__":
    # pseudo-tests de la class «Duree»
    print("[03:05]:", Duree(3, 5))          # __add__
    print("[03:55]:", Duree(3, 5) + 50)
    print("[05:35]:", Duree(3, 5) + 150)
    print("[14:41]:", Duree(13, 51) + 50)
    print("[11:05]:", Duree(10, 3*5) + 50)

    print("[10:00]:", Duree(10, 5) - 5)     # __sub__
    print("[00:05]:", Duree(10, 5) - 600)
    print("[00:00]:", Duree(2, 5) - 600)
