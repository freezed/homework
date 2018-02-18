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

Source:
https://openclassrooms.com/courses/apprenez-a-programmer-en-python/exercises/180
"""

import os
import pickle
# from map import Map
from configuration import BACKUP_FILE, choose_maps_menu, cls, COMMANDS, COMMANDS_LABEL, \
    DIRECTIONS, DIRECTIONS_LABEL, ERR_UNKNOW, get_msg_list, MAP_DIRECTORY, MAP_EXTENTION, maps_name_list, \
    MOVE_STATUS, MOVE_STATUS_MSG, MSG_AVAIBLE_BACKUP, MSG_BACKUP_DONE, MSG_BACKUP_GAME, \
    MSG_CHOOSE_MOVE, MSG_DISCLAMER, MSG_END_GAME, MSG_HELP, MSG_NO_YES, \
    user_select_backup

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
            maps_name_list.append(map_file[: filename_len])

cls()   # clear screen
# Affichage du debut de partie
print(MSG_DISCLAMER)

# Verif si un fichier de sauvegarde est dispo
if os.path.isfile(BACKUP_FILE) is True:
    with open(BACKUP_FILE, 'rb') as backup_file:
        backup_map = pickle.Unpickler(backup_file).load()

    # On demande si l'utilisateur veut charger la sauvegarde
    while user_select_backup not in MSG_NO_YES:
        user_select_backup = input(
                                MSG_AVAIBLE_BACKUP.format(*MSG_NO_YES)
                             ).lower()

    # utilisateur veut la sauvegarde
    if user_select_backup == MSG_NO_YES[1]:
        current_map = backup_map
    else:
        current_map = choose_maps_menu()
else:
    current_map = choose_maps_menu()


# DEBUT DE BOUCLE DE TOUR DE JEU

# Affichage de la carte et de la position de jeu
while current_map.status:
    current_map.map_print()
    print(current_map.status_message)

    # choix du deplacement
    user_select_move = input(MSG_CHOOSE_MOVE.format(
        COMMANDS[1], COMMANDS_LABEL[1])
    ).upper()
    cls()   # clear screen

    if user_select_move == COMMANDS[0]:    # sauvegarder & quitter
        current_map.status = False
        current_map.status_message = MSG_BACKUP_DONE

    elif user_select_move == COMMANDS[1]:  # Affiche l'aide
        current_map.status_message = MSG_HELP
        # liste les directions
        current_map.status_message += get_msg_list(DIRECTIONS, DIRECTIONS_LABEL)
        # liste les commandes
        current_map.status_message += get_msg_list(COMMANDS, COMMANDS_LABEL)

    else:   # traitement du deplacement
        move_status_id = current_map.move_to(user_select_move)
        message = MOVE_STATUS_MSG[MOVE_STATUS[move_status_id]].format(user_select_move)

        # La sortie est atteinte, fin de la boucle
        if MOVE_STATUS[move_status_id] == 'exit':
            current_map.status = False
            current_map.status_message = message

        else:       # sinon on sauvegarde avant de boucler
            current_map.status_message = MSG_BACKUP_GAME
            with open(BACKUP_FILE, 'wb') as backup_file:
                pickle.Pickler(backup_file).dump(current_map)

            current_map.status_message = message


# TODO rester dans la boucle de la partie si la carte n'est pas conforme
if current_map.status is False:
    print(current_map.status_message)
    # fin de la boucle de tour


# Fin de partie
print(MSG_END_GAME)
current_map.map_print()


if __name__ == "__main__":
    """ Starting doctests """
    import doctest
    doctest.testmod()
