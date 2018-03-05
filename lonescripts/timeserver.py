#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
flushserver.py

Time & networking test, talking script
"""
import datetime, select, signal, socket, sys, time

HOST = ''
PORT = 5555
BUFFER = 1024

SERVER_LOG = "{}:{}|{msg}"
MSG_SERVER_STOP = "Server stop"
MSG_START_SERVER = "Server is running, listening on port {}.\n\tPress <ctrl+c> to stop"

inputs = []

def handler(signum, frame):
    """ Catch <ctrl+c> signal for clean stop"""
    print()
    inputs.remove(MAIN_CONNECTION)
    i = 1
    for socket in inputs:
        print(SERVER_LOG.format(*socket.getpeername(), msg="closed client socket"))
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
            except BrokenPipeError:
                print(SERVER_LOG.format(*socket.getpeername(), msg="closed client socket"))
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
    # listening network
    rlist, wlist, xlist = select.select(inputs, [], [], 0.05)

    for socket in rlist:
        # Listen for new client connection
        if socket == MAIN_CONNECTION:
            socket_object, socket_addr = socket.accept()
            inputs.append(socket_object)
            print(SERVER_LOG.format(*socket_addr, msg="connected"))
            msg_time = str(datetime.datetime.now()).split('.')[0]
            socket_object.send(msg_time.encode())

        else:  # receiving data
            data = socket.recv(BUFFER).decode().strip()
            peername = socket.getpeername()

            if data.upper() == "QUIT":
                print(SERVER_LOG.format(*peername, name=None, msg="disconnected"))
                inputs.remove(socket)
                socket.close()

    timestamp = time.localtime()
    if timestamp.tm_sec % 10 == 0:
        broadcast(None, "CLOCK", time.strftime('%Y-%m-%d %H:%M:%S', timestamp))
        time.sleep(1)
