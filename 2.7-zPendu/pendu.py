#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import os
import pickle
from donnees import *
from fonctions import *

 #check_letter, cls, stringalise

# 2.7-zPendu.py: Jeu de pendu avec cumul des scores des differant joueurs

# OpenClassrooms - Apprenez a programmer en Python -
# https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-un-bon-vieux-pendu

# Le joueur donne son nom au debut (enregistrement du score)
# Le script choisit un mot (8 lettres max) au hasard dans une liste
# Le joueur a chaque tour saisit une lettre
# Si la lettre figure dans le mot, l'ordinateur affiche le mot avec
# les lettres deja trouvees. Celles qui ne le sont pas encore sont
# remplacees par des etoiles (*). Le joueur a autant de chances que
# le nombre de lettre du mot. Au dela, perdu.
# Le score: score courant (0 si aucun score deja enregistre), a
# chaque partie, ajoute le nombre de coups restants (non utilise)

# intégrer la date de 1ere partie dans le score
# intégrer la partie au plus fort score
# zerofill les scores

# Constantes
SCORES_FILE = ".scores"
WORD_LIST_FILE = "dicolight.txt"
MAX_TURNS = 12
MAX_NAME_LEN = 7
MIN_NAME_LEN = 2
MSG_DISCLAMER = "Bienvenue au zPendu!\nLe but du jeu est de deviner" + \
    " un mot de 8 lettres max en moins de {} tours.".format(MAX_TURNS)
ASK_NAME = "Votre nom ({} à {} caratères) : "\
    .format(MIN_NAME_LEN, MAX_NAME_LEN)
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

cls()
print(MSG_DISCLAMER)

while (
    len(player_name) < MIN_NAME_LEN or
    len(player_name) > MAX_NAME_LEN or
    player_name.isalnum() is False
):  # Le joueur donne son nom
    player_name = str(input(ASK_NAME)).capitalize()

    if len(player_name) < MIN_NAME_LEN or len(player_name) > MAX_NAME_LEN:
        print(ERR_LETTER_LEN)

    if player_name.isalnum() is False:
        print(ERR_LETTER_ALPHA)

if os.path.isfile(WORD_LIST_FILE) is True:  # Chargement du dictionnaire
    with open(WORD_LIST_FILE, "r") as word_list_file:
        word_list = word_list_file.read().splitlines()
else:
    raise ValueError(ERR_WORD_LIST_FILE)

# Choix du mot cible
target_word = list(word_list[random.randrange(0, len(word_list))])
player_word = list("*" * len(target_word))

# Debut de partie
while game_continue is True:

    while (
        len(letter) != 1
        or letter.isalpha() is False
        or alphabet.count(letter) != 1
    ):  # Le joueur choisi une lettre

            letter = str(input(ASK_LETTER)).upper()

            if len(letter) != 1:
                print(ERR_LETTER_LEN)

            elif letter.isalpha() is False:
                print(ERR_LETTER_ALPHA)

            elif alphabet.count(letter) != 1:
                print(ERR_LETTER_USED)

    # Presence de la lettre?
    if check_letter(letter, target_word) is not False:
        positions = check_letter(letter, target_word)
        for i in positions:
            player_word[i] = letter

    alphabet[alphabet.index(letter)] = '_'
    turns += 1
    if turns == MAX_TURNS or player_word.count("*") == 0:  # Fin de partie?
        game_continue = False

    # Affichage de la fin de tour
    cls()
    print(stringalise(alphabet))
    print("tour : ", turns, "sur ", MAX_TURNS)
    print(stringalise(player_word))


# Fin de partie
points = (MAX_TURNS - turns) + 1
cls()
print(MSG_END_GAME.format(points))
print(stringalise(target_word))

# Affichage du score de la partie et des highscores
if os.path.isfile(SCORES_FILE) is True:  # Ouverture du fichier
    with open(SCORES_FILE, "rb") as scores_file:
        scores = pickle.Unpickler(scores_file).load()

else:
    scores = {player_name: 0}
    print(MSG_1ST_GAME)

# Calcul du score
if scores.get(player_name, False) is False:  # Nouveau joueur
    scores.update({player_name: 0})

scores[player_name] = scores[player_name] + points

# Enregistrement du score
with open(SCORES_FILE, "wb") as scores_file:
    pickle.Pickler(scores_file).dump(scores)

print(MSG_SCORES)
for score in sorted(
    {(points, player) for player, points in scores.items()},
    reverse=True
):
    print("{}\t: {} points".format(score[1], score[0]))
