# Roboc

## Objective of the exercise

Multiplayer maze game over network

All instructions avaiable in the course
_[Apprenez à programmer en Python](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/exercises/181)_
, from **Open Classrooms**.

## Gameplay / roadmap

1. [x] run server
2. [x] choose a map
3. [x] accept client connection
4. when number of connected client is reached, any clients can start the
game with the command 'PLAY'
5. each robot is randomly placed on the map
6. play turn by turn
7. no new client during the game

## Files

 - `server.py`: server script
 - `client.py`: client script
 - `configuration.py`: constants, variables and function
 - `map.py`: object providing a navigable map
 - `connectsocket.py`: socket object providing network
 - `readme.md`: you are reading it!
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

## Bonus
