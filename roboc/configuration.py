"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `roboc`

"""


# CONFIGURATION

MAP_DIRECTORY = 'cartes/'           # repertoire des fichiers carte
MAP_EXTENTION = '.txt'              # extention des fichiers carte
SAVED_GAME_FILENAME = '.backup'     # fichier de sauvegarde
DIRECTIONS = ['N', 'S', 'E', 'O']   # commandes de deplacement
MAZE_ELEMENTS = {'wall': 'O',       # elements dispo dans le labyrinthe
                 'door': '.',
                 'exit': 'U',
                 'robo': 'X',
                 'trace': ' '}
# Issue possible d'un mouvement, garder le OK toujours en fin de liste
MOVE_STATUS = ['bad', 'wall', 'exit', 'door', 'ok']

ERR_ = "#!@?# Oups… "
ERR_MAP_FILE = ERR_ + "carte «{}» inaccessible!"
ERR_MAP_SIZE = ERR_ + "carte «{}», dimensions incorrecte: «{} x {}»"
ERR_MAP_ROBO = ERR_ + "robo est introuvable sur la carte «{}»!"
ERR_PLAGE = ERR_ + "saisir un nombre dans la plage indiquée! "
ERR_SAISIE = ERR_ + "saisir un nombre! "
ERR_UNKNOW = ERR_ + "personne n'est censé arriver ici…"

MIN_MAP_SIDE = 3
MSG_DISCLAMER = "Bienvenue dans Roboc."
MSG_AVAIBLE_MAP = "Cartes disponible: "
MSG_CHOOSE_MAP = "Choississez un numéro de carte: "
MSG_CHOOSE_MOVE = "Votre deplacement: "
MSG_DOOR = "Vous passez une porte"
MSG_SELECTED_MAP = "Vous avez fait le choix #{}, la carte «{}»."
MSG_END_GAME = "Fin de la partie."
MSG_EXIT = "Vous avez atteint la sortie!"

DEBUG = False


# VARIABLES

maps_name_list = list()     # liste des maps proposees a l'utilisateur
user_select_map_id = -1     # carte choisie par l'utilisateur


# FUNCTIONS
def cls():
    """ Efface l'historique de la console """
    import os
    os.system('clear')
    return