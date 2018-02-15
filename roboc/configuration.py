"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `roboc`

"""


# CONFIGURATION

MAP_DIRECTORY = 'cartes/'           # repertoire des fichiers carte
MAP_EXTENTION = '.txt'              # extention des fichiers carte
BACKUP_FILE = '.backup'             # fichier de sauvegarde
DIRECTIONS = ['N', 'S', 'E', 'O']   # commandes de deplacement
MSG_NO_YES = ['non', 'oui']
COMMANDS = {'quit': 'Q',            # commandes d'interuption
            'help':  'H'}
MAZE_ELEMENTS = {'wall': 'O',       # elements dispo dans le labyrinthe
                 'door': '.',
                 'exit': 'U',
                 'robo': 'X',
                 'void': ' '}
# Issue possible d'un mouvement, garder le OK toujours en fin de liste
MOVE_STATUS = ['bad', 'wall', 'exit', 'door', 'ok']
MOVE_STATUS_MSG = {'bad': "Le déplacement «{}» n'est pas autorisé.",
    'wall': "Le déplacement est stoppé par un mur.",
    'exit': "Vous êtes sortit du labyrinte",
    'door': "Vous passez une porte",
    'ok': "Jusqu'ici, tout va bien…"
}

ERR_ = "#!@?# Oups… "
ERR_MAP_FILE = ERR_ + "carte «{}» inaccessible!"
ERR_MAP_SIZE = ERR_ + "carte «{}», dimensions incorrecte: «{} x {}»"
ERR_MAP_ROBO = ERR_ + "robo est introuvable sur la carte «{}»!"
ERR_PLAGE = ERR_ + "saisir un nombre dans la plage indiquée! "
ERR_SAISIE = ERR_ + "saisir un nombre! "
ERR_UNKNOW = ERR_ + "personne n'est censé arriver ici…"

MIN_MAP_SIDE = 3

MSG_DISCLAMER = "Bienvenue dans Roboc."
MSG_AVAIBLE_BACKUP = "Sauvegarde dispo, voulez-vous la charger? ({}/{}) "
MSG_AVAIBLE_MAP = "Cartes disponible: "
MSG_BACKUP_DONE = "La partie a été sauvegardée."
MSG_BACKUP_GAME = "Partie sauvegardé"
MSG_CHOOSE_MAP = "Choississez un numéro de carte: "
MSG_CHOOSE_MOVE = "Votre deplacement: "
MSG_DOOR = "Vous passez une porte"
MSG_SELECTED_MAP = "Vous avez fait le choix #{}, la carte «{}»."
MSG_END_GAME = "Fin de la partie."

DEBUG = False


# VARIABLES


maps_name_list = list()     # liste des maps proposees a l'utilisateur
user_select_backup = str()  # choix utilisateur: la sauvegarde


# FUNCTIONS


def cls():
    """ Efface l'historique de la console """
    import os
    os.system('clear')
    return


def choose_maps_menu():
    """    Affiche le menu de selection des cartes    """
    from map import Map
    # VARIABLES
    user_select_map_id = -1     # choix utilisateur: une carte

    print(MSG_AVAIBLE_MAP)
    i = 0
    for maps_name in maps_name_list:
        print("\t[{}] - {}".format(i, maps_name))
        i += 1

    # Choix de la carte par l'utilisateur
    while user_select_map_id > len(maps_name_list) or user_select_map_id < 0:
        user_select_map_id = input(MSG_CHOOSE_MAP)
        try:
            user_select_map_id = int(user_select_map_id)
            # ? if user_select_map_id is int(): ?
        except ValueError as except_detail:
            if DEBUG:
                print("ValueError: «{}»".format(except_detail))
            else:
                print(ERR_SAISIE)
            user_select_map_id = -1
            continue

        if user_select_map_id > len(maps_name_list) or \
           user_select_map_id < 0:
            print(ERR_PLAGE)

    cls()   # clear screen
    print(MSG_SELECTED_MAP.format(
        user_select_map_id,
        maps_name_list[user_select_map_id]
        ))

    # Fichier carte a recuperer
    map_file = MAP_DIRECTORY + \
        maps_name_list[user_select_map_id] + \
        MAP_EXTENTION

    # instenciation de la carte choisie
    return Map(map_file)
