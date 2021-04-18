#!/usr/bin/env python3
# coding: utf8

"""
Author:     freezed <2160318-free_zed@users.noreply.gitlab.com> 2021-04-13
Licence:    GNU GPL v3

This is a script following
https://gitlab.com/forga/process/fr/embarquement/-/issues/6

The goal is to build durable python script using standard library

This script compute the greater common divisor of 2 integrers
"""
import logging

# MESSAGES
FUNCTION_CALL = "Function is called"
SUBSTRACTION_MADE = "Substraction made"
WRONG_INPUT_ORDER = "Inputs in ascending order"


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
    logging.info(FUNCTION_CALL)
    rest = input_a - input_b
    check = input_b - rest

    while check != 0:
        logging.debug(SUBSTRACTION_MADE)
        input_a = max(input_b, rest)
        input_b = min(input_b, rest)
        rest = input_a - input_b
        check = max(input_b, rest) - min(input_b, rest)

    return rest


if __name__ == "__main__":

    # TESTS
    import doctest

    doctest.testmod()

    # ARGUMENTS, PARAMETERS & OPTIONS
    import argparse
    import sys

    PARSER = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    PARSER.add_argument("INPUT_A", help="The greater integer", type=int)
    PARSER.add_argument("INPUT_B", help="The lower integer", type=int)
    PARSER.add_argument(
        "-v", "--verbose", help="A near mathematics answer", action="store_true"
    )

    ARGS = PARSER.parse_args()

    # CHECKS INPUTS
    if ARGS.INPUT_A <= ARGS.INPUT_B:
        logging.critical(WRONG_INPUT_ORDER)
        sys.exit()

    # DO THE JOB
    else:
        NEW_PGCD = pgcd(ARGS.INPUT_A, ARGS.INPUT_B)

    # RESPONSE
    if ARGS.verbose:
        print(f"PGCD({ARGS.INPUT_A};{ARGS.INPUT_B}) = {NEW_PGCD}")

    else:
        print(NEW_PGCD)
