#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-19
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Testing conditions in try/except statement

https://stackoverflow.com/questions/48864496/adding-if-statement-in-a-try-except-bloc
"""
# ? if user_select_map_id is int(): ?

DEBUG_MODE = [False, True]

for status in DEBUG_MODE:
    print("DEBUG_MODE: {}".format(status))
    number = input("Type a integer: ")
    try:
        number = int(number)
    except ValueError as except_detail:
        if status:
            print("ValueError: «{}»".format(except_detail))
        else:
            print("«{}» is not an integer".format(number))
    else:
        print("Your number {} is an integer".format(number))
