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
    Classe gerant les cartes disponibles et la carte utilisee en cours
    de partie.

    :Example:
    >>> MyMap = Map("cartes/test.txt")
    >>> print(MyMap)

    >>> MyMap.map_print()
    """

    def __init__(self, map_file):
        """
        Initialisation de la carte utilise
        :param map_file:
        """

        # Chargement du fichier carte choisi
        if os.path.isfile(map_file) is True:
            with open(map_file, "r") as map_data:
                self._data_text = map_data.read() # Contient le contenu de la carte en texte
                self._data_list = self._data_text.splitlines() # Contient la carte ligne a ligne
                self._column_nb = len(self._data_list[0]) # Nombre de colonne de la carte (1ere ligne)
                self._line_nb =  len(self._data_list)  # Contient le contenu de la carte en texte

        else:
            raise ValueError('ERR_MAP_FILE')

        line = int(self._line_nb)
        while line == 0:
            if self._data_list[line].find(maze_elmnt['robo']) != -1:
                self._init_position = (line, self._data_list[line].find(maze_elmnt['robo']))

                # la position courante est la position initiale
                self._current_position = self._init_position

            line -= 1


    def __repr__():
        """ Affichage de la carte, via print() """
        return map_print(self)

    def __str__():
        """ Affichage de la carte, via str() """
        return map_print(self)

    def map_print(self):
        """ Affiche la carte avec la position de jeu courante """

    def move_on_map(self, start, move):
        """
        Deplace le «robo» sur la carte

        :param start: coordonnee de depart
        :param move: mouvement souhaite
        :return: 0: wall, 1: sortie, 2: door, 3: ok
        """
        # verifie que le start est dans la carte

        # verifie que le move est possible sur la carte

        # effectue le move et met a jour la carte


        def restore_backup(self, position):
            """ Charge une carte issue d'une sauvegarde """


if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()
