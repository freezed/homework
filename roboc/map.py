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
                self._position = (line, self._data_list[line].find(maze_elmnt['robo']))

            line -= 1

if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()
