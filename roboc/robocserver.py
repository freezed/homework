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
    MOVE_STATUS_MSG, MSG_CHOOSE_MOVE, MSG_CONNECTED_CLIENT, MSG_DISCLAMER, MSG_END_GAME, \
    MSG_HELP, MSG_MINIMUM_CLIENT, MSG_QUIT_GAME, MSG_REQUEST_START, MSG_START_GAME
from connectsocket import ConnectSocket
from map import Map

enough_clients = False
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
MAP_FILENAME = choose_maps_menu()

# Genere la carte
GAME_MAP = Map(MAP_FILENAME)

# Démarre le réseau
GAME_NETWORK = ConnectSocket()

# Attend les connections clients et la commande de départ du jeu
while 1:
    GAME_NETWORK.listen()
    count_clients = GAME_NETWORK.count_clients()

    # attend le nombre mini de client
    if old_count_clients != count_clients:

        if count_clients > MIN_CLIENT_NB:
            broadcast_msg = [MSG_REQUEST_START]
            enough_clients = True

        else:
            sckt = GAME_NETWORK.list_sockets(False, False)[0]

            # envoie le nbre de client aux clients
            broadcast_msg = [
                MSG_MINIMUM_CLIENT.format(MIN_CLIENT_NB),
                MSG_CONNECTED_CLIENT.format(count_clients),
                GAME_NETWORK.list_sockets()
            ]

        # envoi les messages
        for msg in broadcast_msg:
            GAME_NETWORK.broadcast(sckt, "server", msg)

    # attend le go d'un des clients
    if GAME_NETWORK.message.upper() == "PLAY" and enough_clients:
        broadcast_msg = [MSG_START_GAME.format(GAME_NETWORK.u_name)]
        break

    old_count_clients = count_clients


# DEBUT DE BOUCLE DE TOUR DE JEU

# Affichage de la carte tant que status == True
while GAME_MAP.status:
    # Affiche la carte et le message
    GAME_MAP.map_print()
    print(GAME_MAP.status_message)

    # Demande a l'utilisateur son choix du deplacement
    user_move = input(MSG_CHOOSE_MOVE.format(
        COMMANDS[1], COMMANDS_LABEL[1])
                     ).upper()
    cls()   # vide l'ecran de la console

    # Traitement de la commande utilisateur
    if user_move == COMMANDS[0]:    # quitter
        GAME_MAP.status = False
        GAME_MAP.status_message = MSG_QUIT_GAME

    elif user_move == COMMANDS[1]:  # Affiche l'aide
        GAME_MAP.status_message = MSG_HELP
        # liste les directions
        GAME_MAP.status_message += get_msg_list(
            DIRECTIONS, DIRECTIONS_LABEL
        )
        # liste les commandes
        GAME_MAP.status_message += get_msg_list(COMMANDS, COMMANDS_LABEL)

    else:   # Traitement du deplacement
        status = GAME_MAP.move_to(user_move)
        message = MOVE_STATUS_MSG[MOVE_STATUS[status]].format(user_move)
        GAME_MAP.status_message = message

        # La sortie est atteinte, fin de la boucle
        if MOVE_STATUS[status] == 'exit':
            GAME_MAP.status = False

# fin de la boucle de tour

if GAME_MAP.status is False:
    print(GAME_MAP.status_message)

# Fin de partie
print(MSG_END_GAME)
GAME_MAP.map_print()
