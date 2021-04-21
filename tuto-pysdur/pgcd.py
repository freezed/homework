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
LOG_CONSOLE_FORMAT = "[%(name)s] %(levelname)s\t%(message)s"
LOG_FILE_PATH = f"/tmp/{__file__}.log"
LOG_FILE_FORMAT = "[%(asctime)s] " + LOG_CONSOLE_FORMAT
RESULT = "Result : `%s`"
SUBSTRACTION_MADE = "Substraction made : %s - %s"
WRONG_INPUT_ORDER = "Revert input order (`%s < %s`)"

LOGGER = logging.getLogger(__file__)


def argparse_setup():
    """Setting up `argparse` : description & options"""
    import argparse

    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("INPUT_A", help="The greater integer", type=int)
    parser.add_argument("INPUT_B", help="The lower integer", type=int)
    parser.add_argument("-v", "--verbose", help="A verbose answer", action="store_true")
    parser.add_argument(
        "-d",
        "--debug",
        default=False,
        help="Set logging level to DEBUG",
        action="store_true",
    )
    parser.add_argument(
        "-l",
        "--logfile",
        default=False,
        help="Log into a file, not in console",
        action="store_true",
    )
    return parser.parse_args()


def logging_setup(args):
    """
    Setting up `logging` :
        - console or file handler
        - optional DEBUG level
    """

    root_logger = logging.getLogger("")
    loglevel = logging.WARNING

    if args.debug:
        loglevel = logging.DEBUG

    LOGGER.setLevel(loglevel)

    # Add File Handler
    if args.logfile:
        file_hdlr = logging.FileHandler(LOG_FILE_PATH)
        file_hdlr.setFormatter(logging.Formatter(LOG_FILE_FORMAT))
        root_logger.addHandler(file_hdlr)
    # Add Console Handler
    else:
        console_hdlr = logging.StreamHandler()
        console_hdlr.setFormatter(logging.Formatter(LOG_CONSOLE_FORMAT))
        root_logger.addHandler(console_hdlr)


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
    """
    Module's execution management
    I did not test module's import
    """

    # TESTS
    import doctest

    doctest.testmod()

    # SETUPS
    ARGS = argparse_setup()
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
