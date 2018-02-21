#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-06
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

roboc
=====

Jeu permettant de controler un robot dans un labyrinthe.

Voir readme.md
"""

import os
import pickle
from configuration import BACKUP_FILE, choose_maps_menu, cls, COMMANDS, \
    COMMANDS_LABEL, DIRECTIONS, DIRECTIONS_LABEL, get_msg_list, \
    MAP_DIRECTORY, MAP_EXTENTION, MAPS_NAME_LIST, MOVE_STATUS, \
    MOVE_STATUS_MSG, MSG_AVAIBLE_BACKUP, MSG_BACKUP_DONE, MSG_BACKUP_GAME, \
    MSG_CHOOSE_MOVE, MSG_DISCLAMER, MSG_END_GAME, MSG_HELP, MSG_NO_YES, \
    MSG_START_GAME, USER_SELECT_BACKUP

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

# Verif si un fichier de sauvegarde est dispo
if os.path.isfile(BACKUP_FILE) is True:
    with open(BACKUP_FILE, 'rb') as backup_file:
        BACKUP_MAP = pickle.Unpickler(backup_file).load()

    # On demande si l'utilisateur veut charger la sauvegarde
    while USER_SELECT_BACKUP not in MSG_NO_YES:
        USER_SELECT_BACKUP = input(
            MSG_AVAIBLE_BACKUP.format(*MSG_NO_YES)
        ).lower()

    # utilisateur veut la sauvegarde
    if USER_SELECT_BACKUP == MSG_NO_YES[1]:
        CURRENT_MAP = BACKUP_MAP
    else:
        CURRENT_MAP = choose_maps_menu()
else:
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

        # Le premier tour n'a pas ete joue, pas de sauvegarde faite
        if CURRENT_MAP.status_message != MSG_START_GAME:
            CURRENT_MAP.status_message = MSG_BACKUP_DONE

        else:
            CURRENT_MAP.status_message = ""

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

        # La sortie est atteinte, fin de la boucle
        if MOVE_STATUS[status] == 'exit':
            CURRENT_MAP.status = False
            CURRENT_MAP.status_message = message

        else:   # sinon on sauvegarde la partie avant de refaire un tour
            CURRENT_MAP.status_message = MSG_BACKUP_GAME
            with open(BACKUP_FILE, 'wb') as backup_file:
                pickle.Pickler(backup_file).dump(CURRENT_MAP)

            CURRENT_MAP.status_message = message

# fin de la boucle de tour

if CURRENT_MAP.status is False:
    print(CURRENT_MAP.status_message)

# Fin de partie
print(MSG_END_GAME)
CURRENT_MAP.map_print()
