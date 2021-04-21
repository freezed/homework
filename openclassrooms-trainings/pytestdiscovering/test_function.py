#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import function as target

@pytest.fixture()
def product_offline():
    prod_beurre = target.get_product('3017760000109', True)
    prod_oreo = target.get_product('8410000810004', True)
    prod_false = target.get_product('1664', True)
    prod_string = target.get_product('string', True)

    return (prod_beurre, prod_oreo, prod_false, prod_string)

@pytest.fixture()
def product_online():
    prod_beurre = target.get_product('3017760000109')
    prod_oreo = target.get_product('8410000810004')
    return (prod_beurre, prod_oreo)

def test_get_product_stdout(capsys):
    target.get_product('1664', True)
    captured = capsys.readouterr()
    assert captured.out == "File load error : sample/product-1664.json\n"

    target.get_product('string', True)
    captured = capsys.readouterr()
    assert captured.out == "File load error : sample/product-string.json\n"

def test_get_product(product_offline):
    # :Tests OFFLINE:
    prod_beurre, prod_oreo, prod_false, prod_string = product_offline
    assert prod_beurre['product_name'] == 'Le Véritable Petit Beurre'
    assert prod_beurre['nutrition_grades'] == 'e'
    assert prod_beurre['categories_tags'] == [
        'en:sugary-snacks',
        'en:biscuits-and-cakes',
        'en:biscuits',
        'fr:petits-beurres'
    ]

    # better use the file in sample directory
    assert prod_oreo == {'categories_tags': [
        'en:sugary-snacks',
         'en:biscuits-and-cakes',
         'en:biscuits',
         'en:chocolate-biscuits',
         'es:sandwich-cookies'
    ],
    'code': '8410000810004',
    'nutrition_grades': 'e',
    'product_name': 'Biscuit Oreo',
    'url':'https://fr.openfoodfacts.org/product/8410000810004/'}

    assert not prod_false
    assert not prod_string
