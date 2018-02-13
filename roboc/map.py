"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-06
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `roboc`

"""

import os
from configuration import *


class Map:
    """
    Classe gerant les cartes disponibles et la carte utilisee en cours
    de partie.

    :Example:
    >>> EasyMap = Map("cartes/facile.txt")
    >>> TestMap = Map("cartes/test.txt")
    >>> PrisonMap = Map("cartes/prison.txt")
    >>> EmptyMap = Map("cartes/vide.txt")
    >>> TooSmallMap = Map("cartes/trop_petite.txt")
    >>> NoRoboMap = Map("cartes/sans_robo.txt")

    >>> print(EmptyMap.status_message)
    #!@?# Oups… carte «cartes/vide.txt», dimensions incorrecte: «0 x 0»

    >>> print(TooSmallMap.status_message)
    #!@?# Oups… carte «cartes/trop_petite.txt», dimensions incorrecte: «2 x 2»

    >>> print(NoRoboMap.status_message)
    #!@?# Oups… robo est introuvable sur la carte «cartes/sans_robo.txt»!

    >>> print("_column_nb: {}".format(TestMap._column_nb))
    _column_nb: 5

    >>> print("_line_nb: {}".format(TestMap._line_nb))
    _line_nb: 4

    >>> print("_init_robo_position: {}".format(TestMap._init_robo_position))
    _init_robo_position: 20

    >>> TestMap.map_print()
    01234
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
            try:
               self._column_nb = len(map_data_list[0])
            except IndexError:
               self._column_nb = 0

            # nbre de ligne de la carte
            try:
                self._line_nb = len(map_data_list)
            except IndexError:
                self._line_nb = 0

            # positior du robot
            self._robo_position = self._data_text.find(MAZE_ELEMENTS['robo'])

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
            else:
                self._init_robo_position = self._robo_position
                self.status = True

        # Erreur de chargement du fichier
        else:
            self.status = False
            self.status_message = ERR_MAP_FILE.format(map_file)

    # TODO est-ce utile de conserver cette methode?
    def __getattr__(self, name):
        """
        Si un attribut manque a l'appel (_robo_position ou
         _init_robo_position)
        """
        return None

    def map_print(self):
        """ Affiche la carte avec la position de jeu courante """
        print(self._data_text)

    def move_to(self, move):
        """
        Deplace le «robo» sur la carte

        :param move: mouvement souhaite
        :return: key in MOVE_STATUS
        """
        # decompose le mouvement
        direction = move[0]
        distance = move[1:]
        stop = False

        # direction non conforme
        if direction not in DIRECTIONS:
            move_status = 0

        # move possible
        else:
            # pour chaque unite de distance on lit le charactere correspondant
            while distance != 0 or stop:
                next_char = what_is_next_char(direction)
                if next_char == MAZE_ELEMENTS['door']:

                elif next_char == MAZE_ELEMENTS['exit']:

                elif next_char == MAZE_ELEMENTS['wall']:

                else:
                    distance -= 1

            # effectue le mouvement

        return move_status

    def restore_backup(self, position):
        """ Charge une carte issue d'une sauvegarde """


if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()