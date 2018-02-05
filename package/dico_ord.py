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

    :Example:
    >>> fruits = DictionnaireOrdonne()
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

    # Test possible seulement avec python 3.6,
    # voir: www.python.org/dev/peps/pep-0468/
    #>>> print(legumes)
    #{'carotte': 26, 'haricot': 48}

    >>> len(legumes)
    2

    >>> legumes.reverse()

    >>> fruits = fruits + legumes
    >>> fruits
    {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128, 'haricot': 48, 'carotte': 26}

    >>> del fruits['haricot']
    >>> del fruits['betterave']
    ValueError: «'betterave' is not in list»

    >>> 'haricot' in fruits
    False

    >>> 'pomme' in fruits
    True

    >>> legumes['haricot']
    48
    >>> fruits['betterave']
    ValueError: «'betterave' is not in list»

    >>> for cle in legumes:
    ...     print(cle)
    ...
    haricot
    carotte

    >>> fruits.keys()
    ['melon', 'poire', 'pomme', 'prune', 'carotte']

    >>> legumes.keys()
    ['haricot', 'carotte']

    >>> fruits.values()
    [15, 34, 52, 128, 26]

    >>> legumes.values()
    [48, 26]

    #>>> for nom, qtt in legumes.items():
    #...     print("{0} ({1})".format(nom, qtt))
    #...
    #haricot (48)
    #carotte (26)

    #>>> mots = {'olive': 51, 'identite': 43, 'mercredi': 25, 'prout': 218, 'assiette': 8, 'truc': 26}
    #>>> mots_ordonne = DictionnaireOrdonne(mots)
    #>>> mots_ordonne.sort()
    #>>> mots_ordonne
    #{'assiette': 8, 'identite': 43, 'mercredi': 25, 'olive': 51, 'prout': 218, 'truc': 26}
    """

    def __init__(self, **dico):
        """
        On doit pouvoir creer le dictionnaire de plusieurs façons :
        - Vide: aucun parametre
        - Copie d'un dict(): les cles et valeurs contenues dans le
            dictionnaire sont copiees dans l'objet construit.
        - Pre-rempli de cles/valeurs en parametre: pre-remplir
            notre objet avec des couples cles-valeurs passes en
            param (constructeur(cle1 = valeur1, cle2 = valeur2, …))
        Les cles et valeurs doivent etre couplees
        """
        # Creation des attributs qui stokeront les cles et valeurs
        self._keys_list = list()
        self._values_list = list()

        # Si le dictionnaire fournit n'est pas vide, on ajoute les items
        if len(dico) != 0:
            for k, v in dico.items():
                self._keys_list.append(k)
                self._values_list.append(v)

    def __add__(self, other_dict_ord):
        """
        On doit pouvoir ajouter deux dictionnaires ordonnes
        (dico1 + dico2) ; les cles et valeurs du second dictionnaire
        sont ajoutees au premier.
        """
        i = 0
        while i < len(other_dict_ord):
            self._keys_list.append(other_dict_ord._keys_list[i])
            self._values_list.append(other_dict_ord._values_list[i])
            i += 1

        return self

    def __contains__(self, key_to_find):
        """ Cherche une cle dans notre objet (cle in dictionnaire) """

        # TODO utiliser «in»

        try:
            self._keys_list.index(key_to_find)
        except ValueError:
            return False
        else:
            return True

    def __delitem__(self, key_to_del):
        """ Acces avec crochets pour suppression (del objet[cle]) """
        try:
            index_to_del = self._keys_list.index(key_to_del)
        except ValueError as except_detail:
            print("ValueError: «{}»".format(except_detail))
        else:
            del self._keys_list[index_to_del]
            del self._values_list[index_to_del]

    def __iter__(self):
        """
        L'objet doit pouvoir etre parcouru.
        Quand on ecrit for cle in dictionnaire, on doit parcourir
        la liste des cles contenues dans le dictionnaire.
        """

        # TODO revoir __iter__ (+iter()) & items()

        for label in self._keys_list.__iter__():
            yield label

    def __getitem__(self, key_to_get):
        """ Acces aux crochets pour recuperer une valeur (objet[cle]) """
        try:
            find_key = self._keys_list.index(key_to_get)
        except ValueError as except_detail:
            print("ValueError: «{}»".format(except_detail))
        else:
            print(self._values_list[find_key])

    def __len__(self):
        """ Retourne la taille de l'objet grace a la fonction len """
        return len(self._keys_list)

    def __repr__(self):
        """
        Affiche l'objet dans l'interpreteur ou grâce a la fonction
        print: ({cle1: valeur1, cle2: valeur2, …}).
        """
        # contiendra le txt a afficher
        object_repr = list()

        # Si l'objet n'est pas vide
        if len(self._keys_list) != 0:
            for i in range(0, len(self._keys_list)):
                object_repr.append("'{}': {}".format(self._keys_list[i], self._values_list[i]))

        return "{0}{1}{2}".format(
            "{",
            ", ".join(object_repr),
            "}"
        )

    def __setitem__(self, cle, valeur):
        """
        Acces avec crochets pour modif (objet[cle] = valeur). Si la cle
        existe on ecrase l'ancienne valeur, sinon on ajoute le couple
        cle-valeur a la fin
        """
        try:
            index = self._keys_list.index(cle)
            self._keys_list[index] = cle
            self._values_list[index] = valeur
        except ValueError:
            self._keys_list.append(cle)
            self._values_list.append(valeur)

    def __str__(self):
        """
        Methode pour afficher le dictionnaire avec «print()» ou pour
        le convertir en chaine grâce aec «str()». Redirige sur __repr__
        """
        return repr(self)

    def keys(self):
        """
        La methode keys() (renvoyant la liste des cles) doit etre
        mises en œuvre. Le type de retour de ces methodes est laisse
        a votre initiative : il peut s'agir d'iterateurs ou de
        generateurs (tant qu'on peut les parcourir)
        """
        # TODO voir print() vs return list()
        print(self._keys_list)

    def sort(self, reverse=False):
        """
        L'objet doit definir les methodes sort pour le trier et reverse
        pour l'inverser. Le tri de l'objet doit se faire en fonction
        des cles
        """
        # Peut etre un peu overkill… voir methode dans la correction

        # pour trier on stocke les couples de cle & valeur sous forme
        # de tuple dans une liste temporaire
        liste_temporaire = list()

        if len(self._keys_list) != 0:   # Seulement si il y a des donnees
            for i in range(0, len(self._keys_list)):    # on parcour chaque entee
                liste_temporaire.append((self._keys_list[i], self._values_list[i]))

            # Tri des tuples par la valeur par une comprension de liste
            liste_permute = [(val, cle) for cle, val in liste_temporaire]
            liste_triee = [(cle, val) for val, cle in sorted(liste_permute, reverse=reverse)]

            # On range les donnees tries dans attributs de l'objet
            self._keys_list = [cle for cle, val in liste_triee]
            self._values_list = [val for cle, val in liste_triee]

    def reverse(self):
        """
        L'objet doit definir les methodes sort pour le trier et reverse
        pour l'inverser. Le tri de l'objet doit se faire en fonction
        des cles
        """
        return self.sort(reverse=True)

    def items(self):
        """
        La methode values() (renvoyant la liste des valeurs) et
        items() (renvoyant les couples (cle, valeur)) doivent etre
        mises en œuvre. Le type de retour de ces methodes est laisse
        a votre initiative : il peut s'agir d'iterateurs ou de
        generateurs (tant qu'on peut les parcourir)
        """
        i = 0
        while i < len(self._keys_list):
            yield (self._keys_list[i], self._values_list[i])

    def values(self):
        """
        La methode values() (renvoi la liste des valeurs) doit etre
        mises en œuvre. Le type de retour de ces methodes est laisse
        a votre initiative : il peut s'agir d'iterateurs ou de
        generateurs (tant qu'on peut les parcourir)
        """
        # TODO voir print() vs return list()
        print(self._values_list)


if __name__ == "__main__":
    """ Active les doctests """

    import doctest
    doctest.testmod()
