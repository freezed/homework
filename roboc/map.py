#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-06
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `roboc`

"""
import os

class Map:
    """
    Map
    ===

    Classe gerant les cartes disponibles et la carte utilisee en cours
    de partie.


    :Example:
    >>> a = 10
    >>> a + 5
    15
    """

    def __init__(self, path_to_map_file):
        """
        Initialisation de la carte utilisee, mise en cache (grid),

        :param name: nom de la carte chargee
        """
        _column_nb = str() # Nombre de colonne de la carte
        _line_nb = str() # Nombre de ligne de la carte
        _grid = dict() # Contient la carte {(x, y): MAZE_ELEMENT.keys}
        name = str() # nom de la carte utilisee

        # ouvre le fichier

        # parcours le fichier et stocke sont contenu

        # ? verifie la coherence de la carte ?

        # compte les colonnes et lignes


    def move_check(self, start, move):
        """
        Verifie qu'un deplacement est possible

        :param start: coordonnee de depart
        :param move: mouvement souhaite
        :return: 0: wall, 1: sortie, 2: door, 3: ok
        """
        # verifie que le start est dans la carte

        # verifie que le move est possible sur la carte

        # retour


if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()
