#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-06
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

roboc
=====

Jeu permettant de controler un robot dans un labyrinthe
C'est un labyrinthe forme d'obstacles: des murs, des portes et au moins
une sortie. Arrive sur ce point, la partie est terminee.

:Example:
>>> a = 10
>>> a + 5
15

"""

from map import Map
from game import Game
import pickle

# CONFIGURATION
MAP_DIRECTORY = "cartes"
MAP_EXTENTION = "txt"
SAVED_GAME_FILENAME = ".backup"
DIRECTIONS = ["n", "e", "s", "o"] # commandes de deplacement
MAZE_ELEMENTS = {"wall": "O", # elements disponibles dans le labyrinthe
               "door": ".",
               "exit": "U",
               "robo": "X"}

# VARIABLES

# DEBUT DU JEU

#Lister les cartes dispo

#Chercher si une sauvegarde existe

#Choix du joueur

#Debut de partie

#Fin de partie

if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()
