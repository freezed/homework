#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://stackoverflow.com/questions/48729156/how-to-share-values-between-functions-in-python

from random import randrange

a = 20
b = 45

def function1():
    coin = randrange(0, 100)
    a2 = a + coin
    return a2


def function2(coin):
    b2 = b + coin
    return b2

coin = function1() - a
f2 = function2(coin)
print("coin: {}".format(coin))
print("f2: {}".format(f2))
