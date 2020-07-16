#!/usr/bin/env python3
# coding: utf8

"""
Author: freezed <git@freezed.me> 2020-07-16
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [`free_zed/mypsb`](https://gitlab.com/free_zed/mypsb/)
"""


def main(string, n, sep):
    """
    This function reorganize `string` by removing spaces & groups by `n`
    characters separated by `sep`.

    :Tests:
    >>> main("ab c de fgh ijk", 2, "|")
    'ab|cd|ef|gh|ij|k'
    >>> main("ab c de fgh ijk", 3, "_")
    'abc_def_ghi_jk'
    >>> main("ab c de fgh ijk", 4, "/")
    'abcd/efgh/ijk'
    """

    strings = list()

    stack = "".join(string.split(" "))
    steps = round(len(stack) / n)

    while steps != 0:
        strings.append(stack[:n])
        stack = stack[n:]
        steps -= 1

    return sep.join(strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
