#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
server.py

Networking test, client-server talking script
"""
import select, socket

HOST = ''
PORT = 5555
BUFFER = 1024

MSG_NEW_CLIENT = "Nouveau client: {}"
MSG_CLIENT_ID = "Client[{}] {}"
MSG_CLIENT_DISCONNECTED = "Le client {} c'est deconnecté"
MSG_CLOSE_CLIENT = "Fermeture socket client {}"
MSG_SERVER_STOP = "Arrêt du serveur"
MSG_START_SERVER = "Le serveur écoute à présent sur le PORT {}"
MSG_WELCOME = "MSG_WELCOME".encode()

inputs = []

# Creation de la connection
MAIN_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MAIN_CONNECTION.bind((HOST, PORT))
MAIN_CONNECTION.listen(5)
inputs.append(MAIN_CONNECTION)
print(MSG_START_SERVER.format(PORT))

while 1:
    # get the list of sockets which are ready to be read through select
    # timeout 50ms
    rlist, wlist, xlist = select.select(inputs, [], [], 0.05)

    for socket in rlist:
        # Listen for new client connection
        if socket == MAIN_CONNECTION:
            socket_object, socket_addr = socket.accept()
            inputs.append(socket_object)
            print(MSG_NEW_CLIENT.format(socket_addr))

        else:  # receiving data
            data = socket.recv(BUFFER).decode().strip()
            socket.send(MSG_WELCOME)
            print(MSG_CLIENT_ID.format(socket.getpeername(), data))

print(MSG_CLOSE_CLIENT.format(socket.getpeername()))
socket.close()
inputs.remove(socket)

print(MSG_SERVER_STOP)
MAIN_CONNECTION.close()
