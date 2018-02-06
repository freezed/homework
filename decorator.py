#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cours OC/python 3
[Les decorateurs](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-decorateurs)

Author: freezed <git@freezed.me> 2018-02-05
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

:Example:
>>> hello_world()
La fonction appelee: <function hello_world at 0x7f923c95f158> est obsolete.

>>> wait_for()

"""
import time

def my_decorator(function):
    """ test de decorateur """

    def modified_func():
        """ Function modifiee utilisee par le decorateur """
        print("Appel de la fonction: {}".format(function))
        return function()

    return modified_func

def obsolete_exception(function):
    """ Decorateur empechant l'execution d'une fonction obsolete """

    def modd_func():
        print("La fonction appelee: {} est obsolete.".format(function))

    return modd_func

def time_checker(seconds):
    """ Recoit le parametre passe en argument du decorateur """

    def time_decorator(function):
        """ Le decorateur """

        def modified_func(*args, **kwargs):
            """ Function renvoyee par le decorateur """

            tstp_begin = time.time()
            exec_initial_func = function(*args, **kwargs)
            tstp_end = time.time()
            duration = tstp_end - tstp_begin
            if duration > seconds:
                print("La fonction {} à mis {}s pour s'executer".format( \
                        function, round(duration, 1)))

            return exec_initial_func
        return modified_func
    return time_decorator

@obsolete_exception
def hello_world():
    print("Hello World")

@time_checker(3)
def wait_for(name="à vous"):
    input("Bonjour {}, appuyez sur la touche enter…".format(name))


if __name__ == "__main__":
    """ Starting doctests """

    import doctest
    doctest.testmod()
