C'est la copie conforme du corrigé-type! Du coup c'est bien!

Mes commentaires tout de même, en espérant que ce n'est pas le travail d'un élève mais de l'auteur du cours :-o

Je me rends compte que la modélisation que vous avez construite est vraiment très éloignée de la mienne, de fait il m'est difficile de faire une évaluation précise de la pertinence des choix que vous avez faits (imbrication des objets, déplacement du robo, traitement des obstacles, etc.).

J’apprécierais donc, que vous puissiez jeter un œil à mon travail afin que nous puissions échanger mutuellement sur nos modélisations respectives.

J'ai cepandant appris de votre travail et il m'a permis de m'ouvrir les yeux sur des améliorations de mon propre design, qui mériterait sans doutes quelques objets supplémentaires pour le rendre plus évolutif.
En attendant, voici mes quelques commentaires:

- J'ai noté la mise en objet des obstacles permettant de faciliter l'ajout de nouveaux objet facilement
- J'ai trouvé malin le rappel de la méthode de déplacement lorsqu'un chiffre est ajouté à la direction
- J'aurai apprécié un peu plus de commentaires, notamment pour naviguer plus facilement entre les classes
- Bien vu le contrôle d'une carte, mème si les dimension max

- Utilisation de quelques variables/constantes de configuration pour les chaînes de caractères, ça facilite la lecture du code et c'est plus simple à faire évoluer. Par exemple un changement dans les commandes de direction nécessitera des modif identiques à plusieurs endroit du code
- L'accès aux cartes mériterait un bloc try/catch pour s’assurer que le répertoire existe
- Le niveau d'imbrication des objets me semble trop haut: **Carte > Obstacle > TypeObstacle** pour naviguer dans une chaîne de caractère avec des coordonnees sur 2 axes
-
