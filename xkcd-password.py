#!/usr/bin/env python3
# coding: utf8

"""
Author:     freezed <git@freezed.me> 2020-01-16
Licence:    `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/
Inspiration:
    - https://docs.python.org/3/library/secrets.html#recipes-and-best-practices
    - https://xkcd.com/936/
"""
import secrets

with open("/usr/share/dict/words") as f:
    words = [word.strip() for word in f if len(word) == 7]
    for i in range(10):
        password = "-".join(secrets.choice(words) for i in range(5))

        print(password)
