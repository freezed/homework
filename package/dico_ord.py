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

        # Test possible seulement aver python 3:6 ()
        #>>> print(legumes)
        #{'carotte': 26, 'haricot': 48}

        >>> len(legumes)
        2

        >>> legumes.reverse()

        >>> fruits = fruits + legumes
        >>> fruits
        {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128, 'haricot': 48, 'carotte': 26}

        >>> del fruits['haricot']

        #>>> 'haricot' in fruits
        #False

        #>>> legumes['haricot']
        #48

        #>>> for cle in legumes:
        #...     print(cle)
        #...
        #haricot
        #carotte

        #>>> legumes.keys()
        #['haricot', 'carotte']

        #>>> legumes.values()
        #[48, 26]

        #>>> for nom, qtt in legumes.items():
        #...     print("{0} ({1})".format(nom, qtt))
        #...
        #haricot (48)
        #carotte (26)
    """

    def __init__(self, **dico):
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

        self.kl = list()
        self.vl = list()

        if len(dico) != 0:
            for k, v in dico.items():
                self.kl.append(k)
                self.vl.append(v)

    def __repr__(self):
        """
        Affiche l'objet dans l'interpreteur ou grâce a la fonction
        print. L'affichage identique aux dict()
        ({cle1: valeur1, cle2: valeur2, …}).
        """
        content = list()

        if len(self.kl) != 0:
            for i in range(0, len(self.kl)):
                content.append("'{}': {}".format(self.kl[i], self.vl[i]))

        return "{0}{1}{2}".format(
            "{",
            ", ".join(content),
            "}"
        )

    def __setitem__(self, cle, valeur):
        """
        Acces avec crochets pour modif (objet[cle] = valeur)
        Si la cle existe on ecrase l'ancienne valeur, si elle
        n'existe pas on ajoute le couple cle-valeur a la fin
        """
        try:
            index = self.kl.index(cle)
            self.kl[index] = cle
            self.vl[index] = valeur

        except ValueError:
            self.kl.append(cle)
            self.vl.append(valeur)

    def reverse(self):
        """
        L'objet doit definir les methodes sort pour le trier et reverse
        pour l'inverser. Le tri de l'objet doit se faire en fonction
        des cles
        """
        return self.sort(reverse=True)

    def sort(self, reverse=False):
        """
        L'objet doit definir les methodes sort pour le trier et reverse
        pour l'inverser. Le tri de l'objet doit se faire en fonction
        des cles
        """
        # pour trier on stocke les couples de cle & valeur sous forme
        # de tuple dans une liste temporaire
        liste_temporaire = list()

        if len(self.kl) != 0:   # Seulement si il y a des donnees
            for i in range(0, len(self.kl)):    # on parcour chaque entee
                liste_temporaire.append((self.kl[i], self.vl[i]))

            # Tri des tuples par la valeur par une comprension de liste
            liste_permute = [(val, cle) for cle, val in liste_temporaire]
            liste_triee = [(cle, val) for val, cle in sorted(liste_permute, reverse=reverse)]

            # On range les donnees tries dans attributs de l'objet
            self.kl = [cle for cle, val in liste_triee]
            self.vl = [val for cle, val in liste_triee]

    def __len__(self):
        """ Retourne la taille de l'objet grace a la fonction len """
        return len(self.kl)

    def __add__(self, other_dict_ord):
        """
        On doit pouvoir ajouter deux dictionnaires ordonnes
        (dico1 + dico2) ; les cles et valeurs du second dictionnaire
        sont ajoutees au premier.
        """
        i = 0
        while i < len(other_dict_ord):
            self.kl.append(other_dict_ord.kl[i])
            self.vl.append(other_dict_ord.vl[i])
            i += 1

        return self

    def __delitem__(self, item_to_del):
        """ Acces avec crochets pour suppression (del objet[cle]) """
        index_to_del = self.kl.index(item_to_del)
        del self.kl[index_to_del]
        del self.vl[index_to_del]

    #def __contains__():
        #""" Cherche une cle dans notre objet (cle in dictionnaire) """

    #def __delattr__(self):
        #"""
            #Les cles et valeurs doivent etre couplees. Si on cherche
            #a supprimer une cle sa valeur doit etre supprimee.
        #"""

    #def __getitem__():
        #""" Acces avec crochets pour recuperer une valeur (objet[cle]) """

    #def __setattr__():
        #""" Function doc """

    #def generateur():
        #"""
            #L'objet doit pouvoir etre parcouru.
            #Quand on ecrit for cle in dictionnaire, on doit parcourir
            #la liste des cles contenues dans le dictionnaire. A l'instar
            #des dictionnaires, trois methodes keys() (renvoyant la liste
            #des cles), values() (renvoyant la liste des valeurs) et
            #items() (renvoyant les couples (cle, valeur)) doivent etre
            #mises en œuvre. Le type de retour de ces methodes est laisse
            #a votre initiative : il peut s'agir d'iterateurs ou de
            #generateurs (tant qu'on peut les parcourir).
        #"""


if __name__ == "__main__":
    """ Active les doctests """

    import doctest
    doctest.testmod()
