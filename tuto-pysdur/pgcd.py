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
import sys

# MESSAGES
FUNCTION_CALL = "Function `%s` is called"
RESULT = "Result : `%s`"
SUBSTRACTION_MADE = "Substraction made : %s - %s"
WRONG_INPUT_ORDER = "Revert input order (`%s < %s`)"

LOGGER = logging.getLogger(__file__)


def logging_setup(args):
    """Set logging up"""

    loglevel = logging.WARNING
    if args.debug:
        loglevel = logging.DEBUG

    LOGGER.setLevel(loglevel)

    console_hdlr = logging.StreamHandler()
    console_hdlr.setFormatter(
        logging.Formatter("[%(name)s] %(levelname)s\t%(message)s")
    )

    root = logging.getLogger("")
    root.addHandler(console_hdlr)


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
    LOGGER.info(FUNCTION_CALL, "pgcd()")
    rest = input_a - input_b
    check = input_b - rest

    while check != 0:
        input_a = max(input_b, rest)
        input_b = min(input_b, rest)
        LOGGER.debug(SUBSTRACTION_MADE, input_a, input_b)
        rest = input_a - input_b
        check = max(input_b, rest) - min(input_b, rest)

    return rest


if __name__ == "__main__":

    # TESTS
    import doctest

    doctest.testmod()

    # ARGUMENTS, PARAMETERS & OPTIONS
    import argparse

    PARSER = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    PARSER.add_argument("INPUT_A", help="The greater integer", type=int)
    PARSER.add_argument("INPUT_B", help="The lower integer", type=int)
    PARSER.add_argument(
        "-v", "--verbose", help="A near mathematics answer", action="store_true"
    )
    PARSER.add_argument(
        "-d",
        "--debug",
        default=False,
        help="Set logging level to DEBUG",
        action="store_true",
    )
    ARGS = PARSER.parse_args()

    logging_setup(ARGS)

    # CHECKS INPUTS
    if ARGS.INPUT_A <= ARGS.INPUT_B:
        LOGGER.critical(WRONG_INPUT_ORDER, ARGS.INPUT_A, ARGS.INPUT_B)
        sys.exit()

    # DO THE JOB
    else:
        NEW_PGCD = pgcd(ARGS.INPUT_A, ARGS.INPUT_B)

    # POST COMPUTE
    if ARGS.verbose:
        NEW_PGCD = f"PGCD({ARGS.INPUT_A};{ARGS.INPUT_B}) = {NEW_PGCD}"

    if ARGS.debug:
        LOGGER.debug(RESULT, NEW_PGCD)

    else:
        print(NEW_PGCD)
