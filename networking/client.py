#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
client.py

Networking test, client-server talking script
"""
import socket

HOST = "localhost"
PORT = 12800
RECV_BUFFER = 1024

MSG_SERVER_CONNECTED = "Serveur connecté @{}:{}"
MSG_CLOSE_CONNECTION = "Connexion vers [{}:{}] fermée"

STOP_COMMAND = "fin"

SERVER_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_CONNECTION.connect((HOST, PORT))
print(MSG_SERVER_CONNECTED.format(HOST, PORT))

msg_a_envoyer = b""
while msg_a_envoyer != bytes(STOP_COMMAND, 'utf8'):
    msg_a_envoyer = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    SERVER_CONNECTION.send(msg_a_envoyer)
    msg_recu = SERVER_CONNECTION.recv(RECV_BUFFER)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

SERVER_CONNECTION.close()
