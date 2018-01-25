#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Author: freezed <freezed@users.noreply.github.com> 2018-01-25
    Version: 0.1
    Licence: `GNU GPL v3`: http://www.gnu.org/licenses/
"""


class DictionnaireOrdonne:

    """
        Dictionnaire ordonne
        ====================

        Objet ressemblant a un dict, avec des capacitees de tri.

        Les cles et valeurs se trouvant dans des listes de meme
        taille, il suffira de prendre l'indice dans une liste pour
        savoir quel objet lui correspond dans l'autre. Par exemple,
        la cle d'indice 0 est couplee avec la valeur d'indice 0.

        L'objet doit definir les methodes sort pour le trier et reverse
        pour l'inverser. Le tri de l'objet doit se faire en fonction
        des cles.

        On doit pouvoir ajouter deux dictionnaires ordonnes
        (dico1 + dico2) ; les cles et valeurs du second dictionnaire
        sont ajoutees au premier.

        :Example:

        >>> fruits
        {}

        >>> fruits["pomme"] = 52
        >>> fruits["poire"] = 34
        >>> fruits["prune"] = 128
        >>> fruits["melon"] = 15
        >>> fruits
        {'pomme': 52, 'poire': 34, 'prune': 128, 'melon': 15}

        >>> fruits.sort()
        >>> print(fruits)
        {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128}

        >>> legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
        >>> print(legumes)
        {'carotte': 26, 'haricot': 48}

        >>> len(legumes)
        2

        >>> legumes.reverse()
        >>> fruits = fruits + legumes
        >>> fruits
        {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128, 'haricot': 48, 'carotte':26}

        >>> del fruits['haricot']
        >>> 'haricot' in fruits
        False

        >>> legumes['haricot']
        48

        >>> for cle in legumes:
        ...     print(cle)
        ...
        haricot
        carotte

        >>> legumes.keys()
        ['haricot', 'carotte']

        >>> legumes.values()
        [48, 26]

        >>> for nom, qtt in legumes.items():
        ...     print("{0} ({1})".format(nom, qtt))
        ...
        haricot (48)
        carotte (26)
    """

    def __init__(self):
        """
            On doit pouvoir creer le dictionnaire de plusieurs façons :
            - Vide: sans passer aucun parametre
            - Copie d'un dict(): parametre du constructeur un dict() que
                l'on copie par la suite dans notre objet. On peut ainsi
                ecrire constructeur(dictionnaire) et les cles et valeurs
                contenues dans le dictionnaire sont copiees dans l'objet
                construit.
            - Pre-rempli de cles/valeurs en parametre: comme les dict()
                usuels, on doit ici avoir la possibilite de pre-remplir
                notre objet avec des couples cles-valeurs passes en
                param (constructeur(cle1 = valeur1, cle2 = valeur2, …))
            Les cles et valeurs doivent etre couplees
        """

    def __contains__():
        """ Cherche une cle dans notre objet (cle in dictionnaire) """

    def __delattr__(self):
        """
            Les cles et valeurs doivent etre couplees. Si on cherche
            a supprimer une cle sa valeur doit etre supprimee.
        """

    def __getitem__():
        """ Acces avec crochets pour recuperer une valeur (objet[cle]) """

    def __delitem__():
        """ Acces avec crochets pour suppression (del objet[cle]) """

    def __setitem__():
        """
            Acces avec crochets pour modif (objet[cle] = valeur)
            Si la cle existe on ecrase l'ancienne valeur, si elle
            n'existe pas on ajoute le couple cle-valeur a la fin
        """

    def __len__():
        """ Retourne la taille de l'objet grace a la fonction len """

    def __str__(self):
        """
            Affiche l'objet dans l'interpreteur ou grâce a la fonction
            print. L'affichage identique aux dict()
            ({cle1: valeur1, cle2: valeur2, …}).
        """

    def __setattr__():
        """ Function doc """

    def generateur():
        """
            L'objet doit pouvoir etre parcouru.
            Quand on ecrit for cle in dictionnaire, on doit parcourir
            la liste des cles contenues dans le dictionnaire. A l'instar
            des dictionnaires, trois methodes keys() (renvoyant la liste
            des cles), values() (renvoyant la liste des valeurs) et
            items() (renvoyant les couples (cle, valeur)) doivent etre
            mises en œuvre. Le type de retour de ces methodes est laisse
            a votre initiative : il peut s'agir d'iterateurs ou de
            generateurs (tant qu'on peut les parcourir).
        """


if __name__ == "__main__":
    """ Active les doctests """

    import doctest
    doctest.testmod()
