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
    MAP_DIRECTORY, MAP_EXTENTION, maps_name_list, MOVE_STATUS, \
    MOVE_STATUS_MSG, MSG_AVAIBLE_BACKUP, MSG_BACKUP_DONE, MSG_BACKUP_GAME, \
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

# Affichage du debut de partie
cls()   # vide l'ecran de la console
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

# Affichage de la carte tant que status == True
while current_map.status:
    # Affiche la carte et le message
    current_map.map_print()
    print(current_map.status_message)

    # Demande a l'utilisateur son choix du deplacement
    user_move = input(MSG_CHOOSE_MOVE.format(
        COMMANDS[1], COMMANDS_LABEL[1])
    ).upper()
    cls()   # vide l'ecran de la console

    # Traitement de la commande utilisateur
    if user_move == COMMANDS[0]:    # sauvegarder & quitter
        current_map.status = False
        current_map.status_message = MSG_BACKUP_DONE

    elif user_move == COMMANDS[1]:  # Affiche l'aide
        current_map.status_message = MSG_HELP
        # liste les directions
        current_map.status_message += get_msg_list(
            DIRECTIONS, DIRECTIONS_LABEL
        )
        # liste les commandes
        current_map.status_message += get_msg_list(COMMANDS, COMMANDS_LABEL)

    else:   # Traitement du deplacement
        status = current_map.move_to(user_move)
        message = MOVE_STATUS_MSG[MOVE_STATUS[status]].format(user_move)

        # La sortie est atteinte, fin de la boucle
        if MOVE_STATUS[status] == 'exit':
            current_map.status = False
            current_map.status_message = message

        else:   # sinon on sauvegarde la partie avant de refaire un tour
            current_map.status_message = MSG_BACKUP_GAME
            with open(BACKUP_FILE, 'wb') as backup_file:
                pickle.Pickler(backup_file).dump(current_map)

            current_map.status_message = message

# fin de la boucle de tour

if current_map.status is False:
    print(current_map.status_message)

# Fin de partie
print(MSG_END_GAME)
current_map.map_print()
