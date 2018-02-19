# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from labyrinthe import Labyrinthe

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        """ Constructeur de la classe Carte"""
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        """ Contrôleur de l'utilisation de print(self)"""
        return "<Carte {}>".format(self.nom)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        """ Convertisseur de chaîne de caractère en un objet de classe labyrinthe"""
        
        # On sépare la chaîne de caractère dès que \n est repéré
        chaine_grille = chaine.split("\n")
        grille = []
        # On transforme notre chaîne de caractères en liste.
        for l in chaine_grille:
            grille.append(list(l))
            
        # Supprime un espace en bas à droite des labyrinthes, s'il y en a un
        if len(grille[-1])!=len(grille[-2]):
            del grille[-1][-1]
        
        # On récupère les dimensions de notre labyrinthe
        nb_rows = len(grille) # Récupère le nombre de colonnes
        nb_cols = len(grille[0]) # Récupère le nombre de lignes
        
        # On veut maintenant chercher la position de X.
        position_X = False
        # On parcourt ensuite la grille, à la recherche de 'X'
        for i in range(nb_rows):
            for j in range(nb_cols):
                if grille[i][j]=='X':
                    robot = [i,j]
                    position_X = True # Une fois trouvé, on s'arrête
                    break
            if position_X: # Si position_X = 'True' 
                break
        laby = Labyrinthe(robot, grille, chaine)
        return laby