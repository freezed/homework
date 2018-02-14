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

Source: https://openclassrooms.com/courses/apprenez-a-programmer-en-python/exercises/180
"""

import os
from map import Map
from configuration import *
# import pickle

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

# TODO06 Chercher si une sauvegarde existe

# Affichage du debut de partie
cls()   # clear screen
print(MSG_DISCLAMER)
print(MSG_AVAIBLE_MAP)
i = 0
for maps_name in maps_name_list:
    print("\t[{}] - {}".format(i, maps_name))
    i += 1

# Choix de la carte par l'utilisateur
while user_select_map_id > len(maps_name_list) or user_select_map_id < 0:
    user_select_map_id = input(MSG_CHOOSE_MAP)
    try:
        user_select_map_id = int(user_select_map_id)
        # ? if user_select_map_id is int(): ?
    except ValueError as except_detail:
        if DEBUG:
            print("ValueError: «{}»".format(except_detail))
        else:
            print(ERR_SAISIE)
        user_select_map_id = -1
        continue

    if user_select_map_id > len(maps_name_list) or \
       user_select_map_id < 0:
        print(ERR_PLAGE)

print(MSG_SELECTED_MAP.format(user_select_map_id,
      maps_name_list[user_select_map_id]))

# Fichier carte a recuperer
map_file = MAP_DIRECTORY + \
           maps_name_list[user_select_map_id] + \
           MAP_EXTENTION

# instenciation de la carte choisie
current_map = Map(map_file)

# DEBUT DE BOUCLE DE TOUR DE JEU

# Affichage de la carte et de la position de jeu
while current_map.status:
    cls()   # clear screen
    current_map.map_print()

    # TODO07 Utiliser les commandes en capitale
    # choix du deplacement
    user_select_move = input(MSG_CHOOSE_MOVE).lower

    # TODO08 quitter et sauvegarder

    # traitement du deplacement
    move_status_id = current_map.move_to(user_select_move)

    # TODO09 ranger les status dans un dict('ok': MSG_OK, …)
    if MOVE_STATUS[move_status_id] == 'ok':
        print('MSG_OK')

    elif MOVE_STATUS[move_status_id] == 'bad':
        print('MSG_BAD')

    elif MOVE_STATUS[move_status_id] == 'wall':
        print('MSG_WALL')

    elif MOVE_STATUS[move_status_id] == 'door':
        print('MSG_DOOR')

    elif MOVE_STATUS[move_status_id] == 'exit':
        current_map.status = False
        current_map.status_message = MSG_EXIT

    else:  # juste au cas ou…
        raise NotImplementedError(ERR_UNKNOW)

# TODO10 rester dans la boucle si la carte n'est pas conforme
if current_map.status is False:
    print(current_map.status_message)
    # fin de la boucle de tour


# Fin de partie
print(MSG_END_GAME)


if __name__ == "__main__":
    """ Starting doctests """
    import doctest
    doctest.testmod()