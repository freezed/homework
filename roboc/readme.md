# Roboc

## Consignes

> Votre mission est de concevoir et développer un petit jeu permettant de
contrôler un robot dans un labyrinthe. Ce jeu devra être développé en
console pour des raisons d'accessibilité. Je l'ai appelé... Roboc.

> Le jeu est un labyrinthe formé d'obstacles: des murs qui sont tout
simplement là pour vous ralentir, des portes qui peuvent être traversées
et au moins un point par lequel on peut quitter le labyrinthe. Si le
robot arrive sur ce point, la partie est considérée comme gagnée.

Pour les consignes détaillées de l'exercice rendez-vous dans le cours
_[Apprenez à programmer en Python](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/exercises/180)_
d'**Open Classrooms**.

## Utilisation

Je n'ai pas utilisé les éléments de base fourni dans l'exercice. Le
script contient 4 fichiers et 1 répertoire:

 - `roboc.py`: fichier à lancer
 - `configuration.py`: contient les constantes/variables de
 configuration du script, ainsi que les fonctions.
 - `map.py`: fourni les moyens necessaire a l'utilisation d'un fichier
 carte. Controle de coherance sur la carte choise, deplace le robo en
 fonction des commandes du joueur jusqu'en fin de partie.

 - `readme.md`, que vous êtes en train de lire!
 - `cartes`: répertoire contenant les cartes de jeu (fichier `.txt`)

## Contrôle du robot

Le robot est contrôlable grâce à des commandes entrées au clavier. Il
doit exister les commandes suivantes :
 - Q: sauvegarder et quitter la partie en cours
 - N: déplacer vers le nord (haut de l'écran)
 - E: déplacer vers l'est (droite de l'écran)
 - S: déplacer vers le sud (bas de l'écran)
 - O: déplacer vers l'ouest (gauche de l'écran)
 - Chacune des directions ci-dessus suivies d'un nombre permet d'avancer
 de plusieurs cases (ex. E3: 3 cases vers l'est)

## Remarques

Dans les fonctionnalites attendue, la consigne sur la sauvegarde à été
décrites dans 2 consignes qui m'ont semblée floue:
> Enregistrer automatiquement chaque partie à chaque coup pour permettre
de les continuer plus tard

> Q qui doit permettre de sauvegarder et quitter la partie en cours

J'ai choisi d'implementer la sauvegarde par tour, qui sera de fait,
réalisée quand le joueur quitte. Les 2 fonctionnalitées sont ainsi
respectées.

## Bonus

Quelques fonctionnalitées en bonus:

 - contrôle/vérification des cartes, avec quelques cartes «de test», qui
 ne sont pas jouable
 - affichage du recap des commandes (aide), permettant d'ajouter
 d'autres commades utilisateur plus tard
 - la docstring du fichier `map.py` contient des [DocTests](http://sametmax.com/les-docstrings/),
 ça ne fait pas partie du cours, mais c'est un outils facile de
 test/debug que j'utilise et qui reste transparent.
