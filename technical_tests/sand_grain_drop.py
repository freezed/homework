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

    size = len(pile)
    center = int((size - 1) / 2)

    while n != 0:
        pile[center][center] += 1
        do_propagation(pile)
        n -= 1

    # All sand grain are dropped, let's finish propagations
    while True in [4 in row for row in pile]:
        do_propagation(pile)

    return pile


def do_propagation(pile):
    """
    Walk through the pile to propagate sand grains

    :tests:
    >>> test_case = [[0,0,4,0,0],[0,2,0,2,0],[4,0,4,0,4],[0,2,0,2,0],[0,0,4,0,0]]
    >>> do_propagation(test_case)
    >>> print(test_case)
    [[0, 1, 0, 1, 0], [1, 2, 2, 2, 1], [0, 2, 0, 2, 0], [1, 2, 2, 2, 1], [0, 1, 0, 1, 0]]
    """

    size = len(pile)
    x_max, y_max = size - 1, size - 1

    # find cells > 3
    for x in range(size):

        for y in range(size):

            if pile[x][y] > 3:
                pile[x][y] -= 4

                # update west neighbor
                if x < x_max:
                    pile[x + 1][y] += 1
                # update east neighbor
                if x > 0:
                    pile[x - 1][y] += 1
                # update north neighbor
                if y < y_max:
                    pile[x][y + 1] += 1
                # update south neighbor
                if y > 0:
                    pile[x][y - 1] += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
