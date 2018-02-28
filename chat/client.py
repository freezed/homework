#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
client.py

Networking test, client-server talking script
"""
import socket, signal, select, sys

MSG_ARG_ERROR = "Usage: client.py hostname port"

if len(sys.argv) < 3:
    print(MSG_ARG_ERROR)
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

BUFFER = 1024

MSG_SERVER_CONNECTED = "Serveur connecté @{}:{}"
MSG_CLOSE_CONNECTION = "Connexion vers [{}:{}] fermée"

def prompt():
	sys.stdout.write('\n[me]:')
	sys.stdout.flush()

def handler(signum, frame):
    """ Catch <ctrl+c> signal for clean stop"""
    print()
    print(MSG_CLOSE_CONNECTION.format(*(SERVER_CONNECTION.getpeername())))
    SERVER_CONNECTION.send(b"QUIT")
    SERVER_CONNECTION.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

SERVER_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    SERVER_CONNECTION.connect((HOST, PORT))
except ConnectionRefusedError as except_detail:
    print("ConnectionRefusedError: «{}». Unable to connect".format(except_detail))
    sys.exit()

print(MSG_SERVER_CONNECTED.format(HOST, PORT))

while 1:
    inputs = [sys.stdin, SERVER_CONNECTION]
    rlist, wlist, elist = select.select(inputs, [], [])

    for socket in rlist:
        if socket == SERVER_CONNECTION:  # incomming message
            data = socket.recv(BUFFER).decode()
            if not data:
                print(MSG_CLOSE_CONNECTION.format(HOST, PORT))
                sys.exit()
            else:
                #print data
                sys.stdout.write(data)

            prompt()

        else:  # sending message
            msg = sys.stdin.readline().encode()
            SERVER_CONNECTION.send(msg)

SERVER_CONNECTION.close()
