#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-03-23
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

testing kwargs in a function

:Example:
>>> d = {'a2': 'a', 'a3': 'blablabla'}
>>> test(6, **d)
a1:«6», a2:«a», a3:«blablabla»

>>> test(7)
a1:«7», a2:«default value for a2», a3:«default value for a3»

>>> test(8, a2='input a2')
a1:«8», a2:«input a2», a3:«default value for a3»

>>> test(9, a3='input a3')
a1:«9», a2:«default value for a2», a3:«input a3»

>>> test(10, a2='input a2', a3='input a3')
a1:«10», a2:«input a2», a3:«input a3»

====
>>> get_value('symbol', 'name', 'void', 0)
' '

>>> get_value('symbol', 'name', 'void')
[' ']

>>> get_value('tile', 'symbol', 'z', 0) is False
True

>>> get_value(ksel='collect', kval='name', vsel=True)
['needle', 'tube', 'ether']

>>> dico = {'kval': 'tile', 'ksel': 'ressurect', 'vsel': False}
>>> get_value(**dico)
['img/3-blue-transp-30.png', 'img/1-blue-transp-30.png', 'img/2-blue-transp-30.png', 'img/g-orange-transp-30.png', 'img/transp-30.png', 'img/player-30.png', False]

>>> dico = {'kval': 'tile', 'ksel': 'ressurect', 'vsel': False, 'nline': 0}
>>> get_value(**dico)
'img/3-blue-transp-30.png'

"""

LIST = [
    {'symbol': 'n', 'name': 'needle', 'cross': True, 'ressurect': False, 'collect': True, 'tile': 'img/3-blue-transp-30.png'},
    {'symbol': 't', 'name': 'tube', 'cross': True, 'ressurect': False, 'collect': True, 'tile': 'img/1-blue-transp-30.png'},
    {'symbol': 'e', 'name': 'ether', 'cross': True, 'ressurect': False, 'collect': True, 'tile': 'img/2-blue-transp-30.png'},
    {'symbol': 'E', 'name': 'exit', 'cross': True, 'ressurect': False, 'collect': False, 'tile': 'img/g-orange-transp-30.png'},
    {'symbol': ' ', 'name': 'void', 'cross': True, 'ressurect': True, 'collect': False, 'tile': 'img/blue-white-30.png'},
    {'symbol': '.', 'name': 'wall', 'cross': False, 'ressurect': False, 'collect': False, 'tile': 'img/transp-30.png'},
    {'symbol': 'X', 'name': 'player', 'cross': False, 'ressurect': False, 'collect': False, 'tile': 'img/player-30.png'},
    {'symbol': '\n', 'name': 'nlin', 'cross': False, 'ressurect': False, 'collect': False, 'tile': False},
]


def test(a1, **kwargs):
    if 'a2' in kwargs:
        a2 = kwargs['a2']
    else:
        a2 = 'default value for a2'

    if 'a3' in kwargs:
        a3 = kwargs['a3']
    else:
        a3 = 'default value for a3'

    print('a1:«{}», a2:«{}», a3:«{}»'.format(a1, a2, a3))

def get_value(kval, ksel, vsel, nline=False):
    """
    Return a value from LIST

    :param str kval: key of the value returned
    :param str ksel: key of the selection criteria
    :param str vsel: value of the selection criteria
    :return str/bool/…:
    """
    try:
        if nline is False:
            return [element[kval] for element in LIST if element[ksel] == vsel]
        else:
            return [element[kval] for element in LIST if element[ksel] == vsel][nline]
    except IndexError as except_detail:
        # print("IndexError: «{}»".format(except_detail))
        return False

if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()
