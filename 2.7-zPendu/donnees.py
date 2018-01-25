#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# donnee.py : donnee du fichier pendu.py

""" Rassemble les donnee du script pendu.py """

# Constantes
SCORES_FILE = ".scores"
WORD_LIST_FILE = "dicolight.txt"
MAX_TURNS = 12
MAX_NAME_LEN = 7
MIN_NAME_LEN = 2
MSG_DISCLAMER = "Bienvenue au zPendu!\nLe but du jeu est de deviner"+\
    " un mot de 8 lettres max en moins de {} tours.".format(MAX_TURNS)
ASK_NAME = "Votre nom ({} à {} caratères) : ".format(MIN_NAME_LEN, MAX_NAME_LEN)
ASK_LETTER = "Choisissez une lettre : "
ERR_WORD_LIST_FILE = "\t#!@?# Oups… Le dictionnaire n'est pas accesible! #?@!#"
ERR_LETTER_LEN = "\t#!@?# Oups… Saisie trop courte ou trop longue! #?@!#"
ERR_LETTER_ALPHA = "\t#!@?# Oups… Il faut saisir une lettre! #?@!#"
ERR_LETTER_USED = "\t#!@?# Oups… Cette lettre à déjà été jouée! #?@!#"
MSG_END_GAME = "Partie terminée avec {} point(s).\nLe mot mystère était : \n"
MSG_1ST_GAME = "C'était votre 1ère partie ;-)"
MSG_SCORES = "\n-== Les Scores : ==-"

# Variables
game_continue = True
player_name = str()
letter = str()
turns = 0
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
