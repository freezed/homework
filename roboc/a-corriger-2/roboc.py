# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
cartes_enregistrees = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte
            cartes.append( Carte(nom_carte, contenu) )
for nom_fichier in os.listdir("parties_enregistrees"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("parties_enregistrees", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte
            cartes_enregistrees.append( Carte(nom_carte, contenu) )
            
# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# On récupère le nombre de cartes (au cas où on veuille rajouter des cartes)
nb_cartes = len(cartes)
liste_carte = [str(i+1) for i in range(nb_cartes)]
 
# tant que réponse (ie le numéro de la carte souhaitée) n'est pas correcte,
# on demande à l'utilisateur de choisir un labyrinthe   
reponse = 0
while reponse not in (liste_carte):
    print("Entrez un nombre entre 1 et {}".format(nb_cartes))
    reponse = input('Veuillez choisir le labyrinthe que vous voulez:')
    
carte = cartes[int(reponse)-1]
chemin = os.path.join("parties_enregistrees", "{}txt".format(carte.nom)) 
partie_enreg = True 
try:
    with open(chemin) as fichier:
        contenu = fichier.read()
        if not len(contenu)>1:
            partie_enreg = False
except:
     partie_enreg = False

if not partie_enreg:
    # Affichage de la carte sélectionné.
    carte = cartes[int(reponse)-1]
    laby = carte.labyrinthe
    print(laby)
else:
    valid_input=False
    while not valid_input:
        n=input("Il y a une partie enregistree, souhaitez_vous la continuer? (oui/non) > ")
        if n.lower()=='oui':
            for i,carte_en in enumerate(cartes_enregistrees):
                if carte_en.nom == cartes[int(reponse)-1].nom:
                    carte = cartes_enregistrees[i]
                    break
            laby = carte.labyrinthe
            print(laby)
            valid_input=True
        elif n.lower()=='non':
            carte = cartes[int(reponse)-1]
            laby = carte.labyrinthe
            print(laby)
            valid_input=True

print("Taper : 'q' pour quitter la partie et sauvegarder\n\
Déplacements : 'n','s','e','o' suivi du nombre de déplacements dans la direction\n")

partie_finie = False
# On récupère les coordonnées de la sortie avec la méthode trouve_U
sortie = laby.trouve_U()

while not partie_finie:
    direction_valide = False
    while not direction_valide:
        direction = input("> ")
        print()
        # Si l'utilisateur indique 'q' on quitte la partie
        if direction.lower() =='q':
            partie_finie = True
            break
        else:
            if len(direction) == 1:
                # On rajoute 1 si on indique qu'une direction, sans un nombre de pas
                direction = direction + "1"
        direction_valide = laby.valide(direction)          

    if direction.lower() =='q':
            break
    for i in range(int(direction[1:])):
        deplacement = laby.move(direction[0]) # on se déplace si possible
        if deplacement == False:
            print("Aïe, il y a un mur!") # si pas possible, ce message s'affiche
        elif deplacement == True: # Soit que X se retrouve à la sortie U
            laby.actualisation_grille() # On actualise
            laby.update_chaine()
            print(laby) # On affiche
            print('Vous avez trouvé la sortie !')
            partie_finie = True # On termine
            break
        else: # Sinon on poursuit
            laby.actualisation_grille()
        laby.update_chaine()
        print(laby)

    laby.enregistrer(carte.nom)   
    #Puisque la partie est gagnée, on supprime la sauvegarde
    if partie_finie:
        chemin = os.path.join("parties_enregistrees", "{}txt".format(carte.nom))
        os.remove(chemin)     
