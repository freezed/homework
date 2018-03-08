"""
Author: freezed <freezed@users.noreply.github.com> 2018-02-11
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Ce fichier fait partie du projet `roboc`

"""

# CONFIGURATION
# Commandes
# Le code utilise l'index des listes `COMMANDS` & `COMMANDS_LABEL`
#   pour faire le lien entre les 2.
#   Ici vous pouvez ajouter de nouvelles commandes de jeu, elle seront
#   ajoutees a l'aide automatiquement. Mais il faudra ajouter le code
#   leur correspondant dans la condition de traitement du mouvement.
COMMANDS = ['Q', 'H']
# Libelle des commandes d'interuption, conserver l'ordre
COMMANDS_LABEL = ['Quitter', 'Aide']
# Commandes clavier de deplacement
DIRECTIONS = ['N', 'S', 'E', 'O']
# Étiquette des commandes clavier des de deplacements pour l'affichage
#   de l'aide. Garder la correspondance
DIRECTIONS_LABEL = ['nord',
                    'sud',
                    'est',
                    'ouest']

# Pepertoire des fichiers carte
MAP_DIRECTORY = 'cartes/'
# Extention des fichiers carte
MAP_EXTENTION = '.txt'
# Elements dispo dans le labyrinthe
MAZE_ELEMENTS = {'wall': 'O',
                 'door': '.',
                 'exit': 'U',
                 'robo': 'X',
                 'void': ' '}
# Issue possible d'un mouvement, garder le OK toujours en fin de liste
MOVE_STATUS = ['bad', 'wall', 'exit', 'door', 'ok']
MOVE_STATUS_MSG = {
    'bad': "Le déplacement «{}» n'est pas autorisé.",
    'wall': "Le déplacement est stoppé par un mur.",
    'exit': "Vous êtes sortit du labyrinte",
    'door': "Vous passez une porte",
    'ok': "Jusqu'ici, tout va bien…"
}

# Messages d'erreurs
ERR_ = "#!@?# Oups… "
ERR_MAP_FILE = ERR_ + "carte «{}» inaccessible!"
ERR_MAP_SIZE = ERR_ + "carte «{}», dimensions incorrecte: «{} x {}»"
ERR_MAP_ROBO = ERR_ + "robo est introuvable sur la carte «{}»!"
ERR_PLAGE = ERR_ + "saisir un nombre dans la plage indiquée! "
ERR_SAISIE = ERR_ + "saisir un nombre! "
ERR_UNKNOW = ERR_ + "personne n'est censé arriver ici…"

MIN_MAP_SIDE = 3
MIN_CLIENT_NB = 2

MSG_DISCLAMER = "Bienvenue dans Roboc."
MSG_AVAIBLE_MAP = "Cartes disponible: "
MSG_CHOOSE_MAP = "Choississez un numéro de carte: "
MSG_CHOOSE_MOVE = "Votre deplacement ({}:{}): "
MSG_START_GAME = "{} démarre la partie"
MSG_END_GAME = "Fin du jeu."
MSG_QUIT_GAME = "Vous quittez la partie"
# Recapitulatif des commandes
MSG_HELP = "Voici les commandes disponibles:\n"
MSG_SELECTED_MAP = "Vous avez fait le choix #{}, la carte «{}»."
MSG_WAITING_CLIENT = "Nombre de client connecté: \nNombre de client minimum: {}"
MAPS_NAME_LIST = list()     # liste des maps proposees a l'utilisateur

# FONCTIONS


def cls():
    """ Efface l'historique de la console """
    import os
    os.system('clear')
    return


def choose_maps_menu():
    """
    Affiche le menu de selection des cartes

    Recupere les cartes dans un repertoire, demande a l'utilisateur,
    de choisir et effectue quelques tests sur la carte jouee avant de
    creer

    :return: Map object
    """
    from map import Map

    # VARIABLES
    user_select_map_id = -1     # choix utilisateur: une carte

    print(MSG_AVAIBLE_MAP)
    i = 0
    for maps_name in MAPS_NAME_LIST:
        print("\t[{}] - {}".format(i, maps_name))
        i += 1

    # Choix de la carte par l'utilisateur
    while user_select_map_id > len(MAPS_NAME_LIST) or user_select_map_id < 0:
        user_select_map_id = input(MSG_CHOOSE_MAP)
        try:
            user_select_map_id = int(user_select_map_id)
            # ? if user_select_map_id is int(): ?
        except ValueError:
            user_select_map_id = -1
            continue

        if user_select_map_id > len(MAPS_NAME_LIST) or \
           user_select_map_id < 0:
            print(ERR_PLAGE)

    cls()   # vide l'ecran de la console
    print(MSG_SELECTED_MAP.format(
        user_select_map_id,
        MAPS_NAME_LIST[user_select_map_id]
        ))

    # Fichier carte a recuperer
    map_file = MAP_DIRECTORY + \
        MAPS_NAME_LIST[user_select_map_id] + \
        MAP_EXTENTION

    # instenciation de la carte choisie
    return Map(map_file)


def get_msg_list(command, label):
    """
    Formate une chaine pour afficher les commandes et leurs descriptifs

    :type key: lst()
    :param key: liste de commande
    :type label: lst()
    :param label: Texte descriptif des commande associee
    :rtype: str()
    :return: Chaine formatee assemblant les elements en parametres
    """

    # Modele de mise en forme de la liste de chaque element
    TEMPLATE = "\t- «{}»: {}\n"

    # Variable de setour
    result = str()

    for key, value in enumerate(command):
        result += TEMPLATE.format(value, label[key])

    return result
