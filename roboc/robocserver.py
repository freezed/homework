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
    MAP_DIRECTORY, MAP_EXTENTION, MAPS_NAME_LIST, MIN_CLIENT_NB, MOVE_STATUS, \
    MOVE_STATUS_MSG, MSG_CHOOSE_MOVE, MSG_DISCLAMER, MSG_END_GAME, \
    MSG_HELP, MSG_QUIT_GAME, MSG_START_GAME, MSG_WAITING_CLIENT
from ConnectSocket import ConnectSocket

wait_for_clients = True
old_count_clients = int(0)

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

# Affiche le menu de selection de la carte
CURRENT_MAP = choose_maps_menu()

# Démarre le réseau
GAME_NETWORK = ConnectSocket()

# Attend les connections clients et la commande de départ du jeu
while wait_for_clients:
    client_data = GAME_NETWORK.listen()
    count_clients = GAME_NETWORK.count_clients()

    if old_count_clients != count_clients:

        if count_clients > MIN_CLIENT_NB:

            # attend le go d'un des clients
            if client_data[1] == "PLAY":
                wait_for_clients = True
                print(MSG_START_GAME.format(client_data[0]))

            else:
                old_count_clients = GAME_NETWORK.count_clients()
                # envoie le nbre de client aux clients
                # message = MSG_WAITING_CLIENT.format(count_clients, MIN_CLIENT_NB)
                # message += GAME_NETWORK.list_sockets()
                # GAME_NETWORK.broadcast(sender="server", name="server", msg=message)

import pdb; pdb.set_trace()

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
