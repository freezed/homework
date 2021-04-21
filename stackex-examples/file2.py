#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Single variable importation example

:Example:
>>> MyMessage = Message(0)

>>> type(MyMessage)
<class '__main__.Message'>
>>> print(MyMessage)
hello world
>>> repr(MyMessage)
"phrase: hello world|wl: ['hello', 'bonjour', 'ola']"
"""

class Message:

    def __init__(self, index):
        from file1 import WORD_LIST

        self._phrase = WORD_LIST[index] + " world"
        self._word_list = WORD_LIST

    def __repr__(self):
        return "phrase: {}|wl: {}".format(self._phrase, self._word_list)

    def __str__(self):
        return self._phrase

if __name__ == "__main__":
    """ Starting doctests """
    import doctest
    doctest.testmod()
