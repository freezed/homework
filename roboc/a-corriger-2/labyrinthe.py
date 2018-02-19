# -*-coding:Utf-8 -*

import re
import os

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, grille, chaine):
        """ Constructeur de la classe Labyrinthe """
        self.robot = robot
        self.grille = grille
        self.chaine = chaine
        self.porte = self.portes()

    def __repr__(self):
        """ Méthode qui permet d'afficher une instance de classe Labyrinthe"""
        return "<Labyrinthe : \n \n {}>".format(self.grille)
    
    def __str__(self):
        """ Méthode qui permet d'afficher dans la console la grille du labyrinthe"""
        return str(self.chaine)
    
    def portes(self):
        """ Méthode permettant de trouver et de stocker les coordonnées des portes du labyrinthe"""
        porte = []
        nb_rows = len(self.grille)
        nb_cols = len(self.grille[0]) 
        # On veut maintenant chercher les positions des portes.
        # On parcourt la grille, à la recherche de '.'
        for i in range(nb_rows):
            for j in range(nb_cols):
                if self.grille[i][j]=='.':
                    porte.append((i,j))
        return(porte)
    
    def trouve_U(self):
        """ Méthode permettant de trouver la sortie U"""
        nb_rows = len(self.grille)
        nb_cols = len(self.grille[0])

        position_U = False
        # On parcourt ensuite la grille, à la recherche de 'U'
        for i in range(nb_rows):
            for j in range(nb_cols):
                if self.grille[i][j]=='U':
                    sortie = [i,j]
                    position_U = True # Une fois trouvé, on s'arrête
                    break
            if position_U:
                break
        return(sortie)
    
    
    def valide(self, deplacement):
        """ Méthode qui vérifie que l'argument direction/pas est conforme"""
        try:
            assert re.search(r"^[SsOoEeNn]([0-9])*$",deplacement) is not None
        except AssertionError:
            print( "La saisie n'est pas conforme, \n veuillez entrer une direction valide S, O, E, ou N \n \
et le nombre de pas dans cette direction")

        else:
            return('True')
        
        
    def move(self,direction):
        """ Méthode qui renvoie la position du robot à un pas selon l'argument direction"""
        ligne = self.robot[0]
        colonne = self.robot[1]          
            
        if direction == 's':
            dep_ligne = ligne + 1
            if self.grille[dep_ligne][colonne] == 'O':
                return False
            elif self.grille[dep_ligne][colonne] == 'U':
                self.robot = [dep_ligne,colonne]
                return True
            else:
                self.robot = [dep_ligne,colonne]
                
        if direction == 'o':
            dep_col = colonne - 1
            if self.grille[ligne][dep_col] == 'O':
                return False
            elif self.grille[ligne][dep_col] == 'U':
                self.robot = [ligne,dep_col]
                return True
            else:
                self.robot = [ligne,dep_col]
            
        if direction == 'n':
            dep_ligne = ligne - 1
            if self.grille[dep_ligne][colonne] == 'O':
                return False
            elif self.grille[dep_ligne][colonne] == 'U':
                self.robot = [dep_ligne,colonne]
                return True
            else:
                self.robot = [dep_ligne,colonne]
            
        if direction == 'e':
            dep_col = colonne + 1
            if self.grille[ligne][dep_col] == 'O':
                return False
            elif self.grille[ligne][dep_col] == 'U':
                self.robot = [ligne,dep_col]
                return True
            else:
                self.robot = [ligne,dep_col]

        return(self.robot)

            
    def actualisation_grille(self):
        """ Méthode qui actualise la grille du labyrinthe après déplacement du robot"""
        nb_rows = len(self.grille)
        nb_cols = len(self.grille[0])
        # On veut maintenant chercher la position de X.
        # Pour cela, on utilise un booleen
        position_X = False
        # On parcourt ensuite la grille, à la recherche de 'X'
        for i in range(nb_rows):
            for j in range(nb_cols):
                if self.grille[i][j]=='X':
                    robot_ancien = [i,j]
                    position_X = True # Une fois trouvé, on s'arrête
                    break
            if position_X: 
                break
        # On efface le robot
        x = robot_ancien[0]
        y = robot_ancien[1]
        self.grille[x][y] = ' '
        
        # Double boucle pour dessiner/redessiner les portes
        # Avec appel de l'attribu porte défini plus haut
        for i in range(nb_rows):
            for j in range(nb_cols):
                if (i,j) in self.porte:
                    self.grille[i][j] = '.' 
                    self.update_chaine()
        
        # On dessine X
        a = self.robot[0]
        b = self.robot[1]
        self.grille[a][b] = 'X'
        # On actualise
        self.update_chaine()
        
        
    def update_chaine(self):
        """Méthode permettant de mettre à jour self.chaine à partir de self.grille"""
        self.chaine = ""
        for ligne in self.grille:
            self.chaine += "".join(ligne)
            self.chaine += "\n"
        self.chaine = self.chaine[:-1]
    
    
    def enregistrer(self, nom_carte):
        """Méthode permettant d'enregistrer la partie en cours dans un fichier
        Le paramètre nom_carte est le nom donnée à la sauvegarde avec le préfixe 'sauvegarde'"""
        chemin = os.path.join("parties_enregistrees", "{}txt".format(nom_carte))
                
        sauvegarde = open(chemin, "w") 
        sauvegarde.write(self.chaine)
        sauvegarde.close()
    
        
            
            