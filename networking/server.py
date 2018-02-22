#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
server.py

Networking test, client-server talking script
"""
import socket
import select

hote = ''
port = 12800

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.bind((hote, port))
main_connection.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

server_on = True
connected_clients = []
while server_on:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la main_connection en lecture
    # On attend maximum 50ms
    requested_connections, wlist, xlist = select.select([main_connection],
        [], [], 0.05)

    for connexion in requested_connections:
        client_connection, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        connected_clients.append(client_connection)

    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    read_client_list = []
    try:
        read_client_list, wlist, xlist = select.select(connected_clients,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in read_client_list:
            # Client est de type socket
            msg_recu = client.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            print("Reçu {}".format(msg_recu))
            client.send(b"-ok-")
            if msg_recu == "fin":
                server_on = False

print("Fermeture des connexions")
for client in connected_clients:
    client.close()

main_connection.close()
