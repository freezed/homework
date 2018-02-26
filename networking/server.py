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
BUFFER = 1024

MSG_NEW_CLIENT = "Nouveau client: {}"
MSG_CLIENT_ID = "Client[{}] {}"
MSG_CLIENT_DISCONNECTED = "Le client {} c'est deconnecté"
MSG_SERVER_STOP = "Arrêt du serveur"
MSG_START_SERVER = "Le serveur écoute à présent sur le PORT {}"

STOP_COMMAND = "fin"

connections_list = []

# Creation de la connection
MAIN_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MAIN_CONNECTION.bind((HOST, PORT))
MAIN_CONNECTION.listen(5)

server_on = True
connections_list.append(MAIN_CONNECTION)
print(MSG_START_SERVER.format(PORT))

while server_on:
    # get the list of sockets which are ready to be read through select
    # timeout 50ms
    rlist, wlist, xlist = select.select(connections_list, [], [], 0.05)

    for socket in rlist:
        # Listen for new client connection
        if socket == MAIN_CONNECTION:
            socket_object, socket_addr = socket.accept()
            connections_list.append(socket_object)
            print(MSG_NEW_CLIENT.format(socket_addr))

        else:  # receiving data
            print(socket)
            try:
                data = socket.recv(BUFFER)
            except :
                print(MSG_CLIENT_DISCONNECTED.format(socket_addr))
                socket.close()
                connections_list.remove(socket)
                continue

            msg = data.decode()
            socket.send(b"-ok-")
            print(MSG_CLIENT_ID.format(socket.getpeername(), msg))

print(MSG_SERVER_STOP)
MAIN_CONNECTION.close()
