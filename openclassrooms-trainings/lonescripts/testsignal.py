#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1st implementation of signal module https://stackoverflow.com/q/48929752"""
import time
import signal
import os
import sys


def cls():
    """ console clearing """
    os.system('clear')
    return


def handler(signal, frame):
    """ Catch <ctrl+c> signal for clean stop"""
    print("{}, script stops".format(time.strftime('%H:%M:%S')))
    sys.exit(0)


signal.signal(signal.SIGINT, handler)

START_TIME = time.strftime('%H:%M:%S')
PROGRESSION = str()


while True:
    time.sleep(2)
    PROGRESSION += "."
    cls()
    print("{}, script starts\n{}".format(START_TIME, PROGRESSION))
