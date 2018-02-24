#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
server.py

Networking test, client-server talking script
"""
import socket
import select

HOST = ''
PORT = 12800

MSG_NEW_CLIENT = "Nouveau client: {}"
MSG_CLIENT_ID = "Client[{}] {}"
MSG_CLIENT_DISCONNECTED = "Le client {} c'est deconnecté"
MSG_SERVER_STOP = "Arrêt du serveur"
MSG_START_SERVER = "Le serveur écoute à présent sur le PORT {}"

STOP_COMMAND = "fin"

MAIN_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MAIN_CONNECTION.bind((HOST, PORT))
MAIN_CONNECTION.listen(5)
print(MSG_START_SERVER.format(PORT))

server_on = True
connected_clients = []
while server_on:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la MAIN_CONNECTION en lecture
    # On attend maximum 50ms
    requested_connections, wlist, xlist = select.select(
        [MAIN_CONNECTION],
        [], [], 0.05
        )

    for connexion in requested_connections:
        client_connection, infos_connexion = connexion.accept()

        # On ajoute le socket connecté à la liste des clients
        connected_clients.append(client_connection)

        # id client
        fileno = client_connection.fileno()
        print(MSG_NEW_CLIENT.format(fileno))

    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    read_client_list = []
    try:
        read_client_list, wlist, xlist = select.select(
            connected_clients,
            [], [], 0.05
            )
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in read_client_list:

            # Client est de type socket
            msg_recu = client.recv(1024)

            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            client.send(b"-ok-")

            print(MSG_CLIENT_ID.format(client.fileno(), msg_recu))

            if msg_recu == STOP_COMMAND:
                client.send(bytes(MSG_SERVER_STOP, 'utf8'))
                server_on = False

print(MSG_SERVER_STOP)
for client in connected_clients:
    client.close()

MAIN_CONNECTION.close()
