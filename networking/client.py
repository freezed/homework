#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
client.py

Networking test, client-server talking script
"""
import socket, sys, select


def prompt():
	sys.stdout.write('[me] ')
	sys.stdout.flush()


MSG_ARG_ERROR = "Usage: client.py hostname port"

if len(sys.argv) < 3:
    print(MSG_ARG_ERROR)
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

BUFFER = 1024

MSG_SERVER_CONNECTED = "Serveur connecté @{}:{}"
MSG_CLOSE_CONNECTION = "Connexion vers [{}:{}] fermée"

STOP_COMMAND = "fin"

SERVER_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    SERVER_CONNECTION.connect((HOST, PORT))
except ConnectionRefusedError as except_detail:
    print("ConnectionRefusedError: «{}». Unable to connect".format(except_detail))
    sys.exit()

print(MSG_SERVER_CONNECTED.format(HOST, PORT))
prompt()

while 1:
    sockets_list = [sys.stdin, SERVER_CONNECTION]
    rlist, wlist, elist = select.select(sockets_list, [], [])

    for socket in sockets_list:
        if socket == SERVER_CONNECTION:
            data = socket.recv(BUFFER)
            if not data:
                print('\nDisconnected from the chat server')
                sys.exit()
            else:
                #print data
                msg = data.decode()
                sys.stdout.write(msg)

        #user entered a message
        else:
            msg = sys.stdin.readline()
            msg_a_envoyer = msg.encode()
            SERVER_CONNECTION.send(msg_a_envoyer)
            prompt()

SERVER_CONNECTION.close()
