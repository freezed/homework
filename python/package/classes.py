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
        return "{}:{}".format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        """L'objet a ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        # On va copier self dans l'objet cree pour avoir la même duree
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        nouvelle_duree.sec += objet_a_ajouter  # On ajoute la duree

        if nouvelle_duree.sec >= 60:  # Si le nombre de secondes >= 60
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60

        return nouvelle_duree  # On renvoie la nouvelle duree
