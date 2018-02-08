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

# from map import *
# from game  import *
import os
import pickle

# CONFIGURATION
MAP_DIRECTORY = 'cartes'     # repertoire des fichiers carte
MAP_EXTENTION = '.txt'       # extention des fichiers carte
SAVED_GAME_FILENAME = '.backup'     # fichier de sauvegarde
DIRECTIONS = ['n', 'e', 's', 'o']   # commandes de deplacement
MAZE_ELEMENTS = {'wall':'O', # elements disponibles dans le labyrinthe
                 'door':'.',
                 'exit':'U',
                 'robo':'X'}
MSG_DISCLAMER = "Bienvenue dans Roboc."
MSG_CHOOSE_MAP = "Choississez une carte: "


# VARIABLES
maps_name_list = list()  # liste des maps proposees a l'utilisateur

# FONCTIONS


# DEBUT DU JEU

# Recuperation de la liste des cartes
try:
    maps_avaiable = os.listdir(MAP_DIRECTORY)
except FileNotFoundError as except_detail:
    print("FileNotFoundError: «{}»".format(except_detail))
else:
    for map_file in maps_avaiable:
        filename_len = len(map_file) - len(MAP_EXTENTION)

        # garde les fichiers avec la bonne extention
        if map_file[filename_len:] == MAP_EXTENTION:
            maps_name_list.append(map_file[:filename_len])

i = 0
print(MSG_DISCLAMER)
print(MSG_CHOOSE_MAP)
for maps_name in maps_name_list:
    print("\t[{}] - {}".format(i, maps_name))
    i += 1


#Lister les cartes dispo

#Chercher si une sauvegarde existe

#Choix du joueur

#Debut de partie

#Fin de partie

if __name__ == "__main__":
    """ Starting doctests """
#    import doctest
#    doctest.testmod()
