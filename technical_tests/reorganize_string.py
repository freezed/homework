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
    >>> main("ab c de fgh ijk", 3, "|")
    'abc|def|ghi|jk'
    """
    answer = ""

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
