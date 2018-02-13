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
    >>> MiniMap = Map("cartes/mini.txt")
    >>> PrisonMap = Map("cartes/prison.txt")
    >>> EmptyMap = Map("cartes/vide.txt")
    >>> TooSmallMap = Map("cartes/trop_petite.txt")
    >>> NoRoboMap = Map("cartes/sans_robo.txt")

    >>> print(EmptyMap.status_message)
    #!@?# Oups… carte «cartes/vide.txt», dimensions incorrecte: «0 x 0»
    >>> print(TooSmallMap.status_message)
    #!@?# Oups… carte «cartes/trop_petite.txt», dimensions incorrecte: «3 x 2»
    >>> print(NoRoboMap.status_message)
    #!@?# Oups… robo est introuvable sur la carte «cartes/sans_robo.txt»!

    >>> print("_column_nb: {}".format(TestMap._column_nb))
    _column_nb: 6
    >>> print("_line_nb: {}".format(TestMap._line_nb))
    _line_nb: 4
    >>> print("_init_robo_position: {}".format(TestMap._init_robo_position))
    _init_robo_position: 20

    >>> TestMap.move_to("n3")
    4
    >>> TestMap.map_print()
    01X34
    abcde
    ABCDE
    zy wv
    >>> TestMap.move_to("o2")
    4
    >>> TestMap.move_to("s3")
    4
    >>> TestMap.move_to("e4")
    4

    >>> MiniMap.move_to("o1")
    1
    >>> MiniMap.move_to("Z1")
    0
    >>> MiniMap.move_to("4")
    0
    >>> MiniMap.move_to("e1")
    2
    >>> MiniMap.map_print()
    000
     XU
    000
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
               self._column_nb = len(map_data_list[0]) +1
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
                # TODO est-ce utile de concerver la pos initiale?
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
        goal = int(move[1:])
        steps = 0
        move_status = 4

        # direction non conforme
        if direction not in DIRECTIONS:
            move_status = 0

        else:
            # import pdb; pdb.set_trace()
            # pour chaque pas on recupere la position suivante
            while steps < goal or move_status != 4:
                steps += 1
                if direction == DIRECTIONS[0]:      # nord
                    next_position = self._robo_position - self._column_nb

                elif direction == DIRECTIONS[1]:    # sud
                    next_position = self._robo_position + self._column_nb

                elif direction == DIRECTIONS[2]:    # est
                    next_position = self._robo_position + 1

                elif direction == DIRECTIONS[3]:    # ouest
                    next_position = self._robo_position - 1

                else:   # juste au cas ou
                    raise NotImplementedError(ERR_)

                # verifie quelle est la case du prochain pas
                next_char = self._data_text[next_position]
                if next_char == MAZE_ELEMENTS['wall']:
                    move_status = 1

                elif next_char == MAZE_ELEMENTS['exit']:
                    self._robo_position = next_position
                    move_status = 2

                elif next_char == MAZE_ELEMENTS['door']:
                    self._robo_position = next_position
                    move_status = 3

                else:
                    self._robo_position = next_position

            # supprime le robo de son emplacement precedent
            self._data_text = self._data_text.replace(
                MAZE_ELEMENTS['robo'],
                MAZE_ELEMENTS['trace']
            )
            # place le robo sur sa nouvelle position
            self._data_text = self._data_text[:self._robo_position] + \
                MAZE_ELEMENTS['robo'] + \
                self._data_text[self._robo_position +1:]

        return move_status

    # def restore_backup(self, position):
        # """ Charge une carte issue d'une sauvegarde """


if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()