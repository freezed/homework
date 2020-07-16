#!/usr/bin/env python3
# coding: utf8

"""
Author: freezed <git@freezed.me> 2020-07-16
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [`free_zed/mypsb`](https://gitlab.com/free_zed/mypsb/)
"""


def main(pile, n):
    """
    This function returns the situation of a sand `pile` after droping `n`
    sand grain on top of it.


    1. Sand pile is a square table of uneven size (viewed from up)
    1. Sand grain is always dropped on center of pile.
    1. When a cell had 4 grains inside, these grains moves on the near 4th cells
    1. Grains going out the pile are losts

    :Tests:
    >>> main([[1,1,1],[1,1,1],[1,1,1]],1)
    [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
    >>> main([[1,1,1],[1,1,1],[1,1,1]],2)
    [[1, 1, 1], [1, 3, 1], [1, 1, 1]]
    >>> main([[1,1,1],[1,1,1],[1,1,1]],3)
    [[1, 2, 1], [2, 0, 2], [1, 2, 1]]
    >>> main([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],1)
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    >>> main([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],3)
    [[1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 2, 0, 2, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1]]
    >>> main([[0,0,3,0,0],[0,0,3,0,0],[3,3,3,3,3],[0,0,3,0,0],[0,0,3,0,0]],1)
    [[0, 1, 0, 1, 0], [1, 2, 2, 2, 1], [0, 2, 0, 2, 0], [1, 2, 2, 2, 1], [0, 1, 0, 1, 0]]
    """

    center = int((len(pile) - 1) / 2)

    while n != 0:

        if pile[center][center] < 3:
            pile[center][center] += 1

        n -= 1

    return pile


if __name__ == "__main__":
    import doctest

    doctest.testmod()
