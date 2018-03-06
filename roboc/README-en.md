# Roboc

## Exercice instructions

Multiplayer maze game over network

All instructions avaiable in the course
_[Apprenez à programmer en Python](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/exercises/181)_
, from **Open Classrooms**.

## Gameplay

1. run server
2. choose a map
3. accept client connection
4. for each client a new robot is created
5. each robot is randomly placed on the map
6. when number of connected client is reached, any clients can start the
game with the command 'c'
7. no new client during the game

## Usage

 - `server.py`: server script
 - `client.py`: client script
 - `configuration.py`: configuration file
 - `map.py`: map object

 - `readme.md`, you are reading it!
 - `cartes`: place for map files (ext. `.txt`)

## Commands

The robot is controllable by keyboard commands. The following commands
must exist:
 - Q: Quit game
 - N: move north (up)
 - E: move east (right)
 - S: move south (down)
 - O: move west (left)
 - Each of the above directions followed by a number allows you to
 advance several squares (e. g. E3:3 squares to the east)

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
