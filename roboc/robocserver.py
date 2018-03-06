#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-06
Version: 0.2
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

roboc
=====

A multiplayer maze game over network

This is the server script, see readme.md for more details
"""

import os
from configuration import choose_maps_menu, cls, COMMANDS, \
    COMMANDS_LABEL, DIRECTIONS, DIRECTIONS_LABEL, get_msg_list, \
    MAP_DIRECTORY, MAP_EXTENTION, MAPS_NAME_LIST, MOVE_STATUS, \
    MOVE_STATUS_MSG, MSG_CHOOSE_MOVE, MSG_DISCLAMER, MSG_END_GAME, \
    MSG_HELP, MSG_QUIT_GAME

# DEBUT DU JEU

# Recuperation de la liste des cartes
try:
    MAPS_AVAIBLE = os.listdir(MAP_DIRECTORY)
except FileNotFoundError as except_detail:
    print("FileNotFoundError: «{}»".format(except_detail))
else:
    for map_file in MAPS_AVAIBLE:
        filename_len = len(map_file) - len(MAP_EXTENTION)

        # garde les fichiers avec la bonne extention
        if map_file[filename_len:] == MAP_EXTENTION:
            MAPS_NAME_LIST.append(map_file[: filename_len])

# Affichage du debut de partie
cls()   # vide l'ecran de la console
print(MSG_DISCLAMER)

CURRENT_MAP = choose_maps_menu()


# DEBUT DE BOUCLE DE TOUR DE JEU

# Affichage de la carte tant que status == True
while CURRENT_MAP.status:
    # Affiche la carte et le message
    CURRENT_MAP.map_print()
    print(CURRENT_MAP.status_message)

    # Demande a l'utilisateur son choix du deplacement
    user_move = input(MSG_CHOOSE_MOVE.format(
        COMMANDS[1], COMMANDS_LABEL[1])
                     ).upper()
    cls()   # vide l'ecran de la console

    # Traitement de la commande utilisateur
    if user_move == COMMANDS[0]:    # quitter
        CURRENT_MAP.status = False
        CURRENT_MAP.status_message = MSG_QUIT_GAME

    elif user_move == COMMANDS[1]:  # Affiche l'aide
        CURRENT_MAP.status_message = MSG_HELP
        # liste les directions
        CURRENT_MAP.status_message += get_msg_list(
            DIRECTIONS, DIRECTIONS_LABEL
        )
        # liste les commandes
        CURRENT_MAP.status_message += get_msg_list(COMMANDS, COMMANDS_LABEL)

    else:   # Traitement du deplacement
        status = CURRENT_MAP.move_to(user_move)
        message = MOVE_STATUS_MSG[MOVE_STATUS[status]].format(user_move)
        CURRENT_MAP.status_message = message

        # La sortie est atteinte, fin de la boucle
        if MOVE_STATUS[status] == 'exit':
            CURRENT_MAP.status = False

# fin de la boucle de tour

if CURRENT_MAP.status is False:
    print(CURRENT_MAP.status_message)

# Fin de partie
print(MSG_END_GAME)
CURRENT_MAP.map_print()
