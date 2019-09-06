#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
testsocketclose.py

https://stackoverflow.com/q/32019274/6709630
"""
import signal, socket, sys, time

def handler(signum, frame):
    """ Catch <ctrl+c> signal for clean stop"""
    print('\nNice exit')
    connection.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

# Creation de la connection
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind(('localhost', 5555))
connection.listen(5)

while 1:
    print("Socket open:\n{}\nExit with <ctrl+c>".format(connection))
    time.sleep(2)
