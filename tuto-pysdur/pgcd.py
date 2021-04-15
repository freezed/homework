#!/usr/bin/env python3
# coding: utf8

"""
Author: freezed <2160318-free_zed@users.noreply.gitlab.com> 2021-04-13
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This is a script following
https://gitlab.com/forga/process/fr/embarquement/-/issues/6

The goal is to build durable python script using standard library

:Tests:
>>> pgcd(561, 357)
51
"""


def pgcd(input_a, input_b):
    """
    This function find the Greatest Common Divisor (PGCD in French)
    between input_a & input_b

    :Tests:
    >>> pgcd(561, 357)
    51
    >>> pgcd(63, 42)
    21
    >>> pgcd(21, 15)
    3
    >>> pgcd(910, 42)
    14
    """
    rest = input_a - input_b
    check = input_b - rest

    while check != 0:
        input_a = max(input_b, rest)
        input_b = min(input_b, rest)
        rest = input_a - input_b
        check = max(input_b, rest) - min(input_b, rest)

    print(rest)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
