"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-06
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `roboc`

"""

import os
from configuration import MAZE_ELEMENTS, ERR_MAP_FILE, MIN_MAP_SIDE, \
    ERR_MAP_SIZE, ERR_MAP_ROBO


class Map:
    """
    Classe gerant les cartes disponibles et la carte utilisee en cours
    de partie.

    :Example:
    >>> TestMap = Map("cartes/test.txt")

    >>> PrisonMap = Map("cartes/prison.txt")

    >>> print("_data_text: {}".format(TestMap._data_text))
    _data_text: O1234
    abcde
    ABCDE
    zyXwv

    >>> print("_column_nb: {}".format(TestMap._column_nb))
    _column_nb: 5

    >>> print("_line_nb: {}".format(TestMap._line_nb))
    _line_nb: 4

    >>> print("_init_robo_position: {}".format(TestMap._init_robo_position))
    _init_robo_position: None

    >>> print("_robo_position: {}".format(TestMap._robo_position))
    _robo_position: None

    >>> type(TestMap._data_text)
    <class 'str'>

    >>> TestMap.map_print()
    O1234
    abcde
    ABCDE
    zyXwv

    """

    def __init__(self, map_file):
        """
        Initialisation de la carte utilise
        :param map_file:
        """
        # Chargement du fichier carte choisi
        if os.path.isfile(map_file) is True:
            with open(map_file, "r") as map_data:
                # contenu de la carte en texte
                self._data_text = map_data.read()
                # contenu de la carte ligne a ligne
                map_data_list = self._data_text.splitlines()
                # nbre de colonne de la carte (1ere ligne)
                self._column_nb = len(map_data_list[0])
                # nbre de ligne de la carte
                self._line_nb = len(map_data_list)
                # positior du robot
                self._robo_position = self._data_text.find(MAZE_ELEMENTS['robo'])

        # Erreur de chargement du fichier
        else:
            self.status = False
            self.status_message = ERR_MAP_FILE.format(map_file)

        # Quelques controle sur la carte:
        # - a t elle des dimensions mini?
        if self._column_nb < MIN_MAP_SIDE or self._line_nb < MIN_MAP_SIDE:
            self.status = False
            self.status_message = ERR_MAP_SIZE.format(
                map_file, self._column_nb, self._line_nb
            )

        # - a t elle un robo ( TODO : hors mur)?
        elif self._robo_position == -1:
            self.status = False
            self.status_message = ERR_MAP_ROBO.format(map_file)

        # - a t elle une sortie (dans mur) TODO?
        # - a t elle du mur tout autour TODO?

        self._init_robo_position = self._robo_position
        self.status = True

    def __getattr__(self, name):
        """
        Si un attribut manque a l'appel (_robo_position ou
         _init_robo_position)
        """
        return None

    def map_print(self):
        """ Affiche la carte avec la position de jeu courante """
        print(self._data_text)

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