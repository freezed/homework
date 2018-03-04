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

SERVER_LOG = "{}:{}|{name}|{msg}"
MSG_DISCONNECTED = "<gone away to infinity, and beyond>"
MSG_SERVER_STOP = "Server stop"
MSG_START_SERVER = "Server is running, listening on port {}.\n\tPress <ctrl+c> to stop"
MSG_USER_IN = "<entered the chatroom>"
MSG_WELCOME = "Welcome. First do something usefull and type your name: ".encode()

inputs = []
user_name = []

def handler(signum, frame):
    """ Catch <ctrl+c> signal for clean stop"""
    print()
    inputs.remove(MAIN_CONNECTION)
    i = 1
    for socket in inputs:
        print(SERVER_LOG.format(*socket.getpeername(), name=user_name[i], msg="closed client socket"))
        socket.close()
        i += 1
    inputs.clear()
    print(MSG_SERVER_STOP)
    MAIN_CONNECTION.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

def broadcast(sender, name, message):
    # send message to all clients, except the sender
    message = "\n~{}~ {}".format(name, message)
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
user_name.append("MAIN_CONNECTION")
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
            user_name.append(False)
            print(SERVER_LOG.format(*socket_addr, name="unknow", msg="connected"))
            socket_object.send(MSG_WELCOME)

        else:  # receiving data
            data = socket.recv(BUFFER).decode().strip()
            peername = socket.getpeername()
            s_idx = inputs.index(socket)
            uname = user_name[s_idx]

            if data.upper() == "QUIT":
                print(SERVER_LOG.format(*peername, name=uname, msg="disconnected"))
                broadcast(socket, uname, MSG_DISCONNECTED)
                inputs.remove(socket)
                user_name.pop(s_idx)
                socket.close()

            elif user_name[s_idx] is False:  # setting username
                # insert username naming rule here
                user_name[s_idx] = data
                socket.send("Hi, {}".format(user_name[s_idx]).encode())
                print(SERVER_LOG.format(*peername, name=data, msg="set user name"))
                broadcast(socket, user_name[s_idx], MSG_USER_IN)

            elif data:
                print(SERVER_LOG.format(*peername, name=uname, msg=data))
                broadcast(socket, uname, data)

            else:
                print("Server encountered an unknown case")
                import pdb; pdb.set_trace()
