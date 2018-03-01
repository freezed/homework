#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
server.py

Networking test, client-server talking script
"""
import select, signal, socket, sys

HOST = ''
PORT = 5555
BUFFER = 1024

MSG_NEW_CLIENT = "Nouveau client: {}"
MSG_CLIENT_ID = "Client[{}] {}"
MSG_CLIENT_DISCONNECTED = "Le client {} c'est deconnecté"
MSG_DISCONNECTED = "<À quitté le chat>"
MSG_CLOSE_CLIENT = "Fermeture socket client {}"
MSG_SERVER_STOP = "Arrêt du serveur"
MSG_START_SERVER = "Serveur écoute sur le port {}. <ctrl+c> pour stopper le serveur."
MSG_WELCOME = "MSG_WELCOME".encode()

inputs = []

def handler(signum, frame):
    """ Catch <ctrl+c> signal for clean stop"""
    print()
    inputs.remove(MAIN_CONNECTION)
    for socket in inputs:
        print(MSG_CLOSE_CLIENT.format(socket.getpeername()))
        socket.close()
    inputs.clear()
    print(MSG_SERVER_STOP)
    MAIN_CONNECTION.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

def broadcast(sender, message):
    # send message to all clients, except the sender
    message = "\n~{}:{}~ {msg}".format(*sender.getpeername(), msg=message)
    for socket in inputs:
        if socket != MAIN_CONNECTION and socket != sender:
            try:
                socket.send(message.encode())
            except :
                socket.close()
                inputs.remove(socket)

# Creation de la connection
MAIN_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MAIN_CONNECTION.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
            broadcast(socket_object, MSG_NEW_CLIENT.format(socket_addr))
            socket_object.send(MSG_WELCOME)

        else:  # receiving data
            data = socket.recv(BUFFER).decode().strip()
            if data.upper() == "QUIT":
                print(MSG_CLIENT_DISCONNECTED.format(socket.getpeername()))
                broadcast(socket, MSG_DISCONNECTED)
                inputs.remove(socket)
                socket.close()

            elif data:
                print(MSG_CLIENT_ID.format(socket.getpeername(), data))
                broadcast(socket, data)
