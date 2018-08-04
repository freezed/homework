#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-08-03
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

Basic implementation of PyMySQL

-- Local DB --
CREATE DATABASE loff CHARACTER SET 'utf8';
USE loff;

CREATE TABLE category(
    `id`INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(200) UNIQUE

)ENGINE=InnoDB;

CREATE TABLE product(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `code` BIGINT UNSIGNED NOT NULL UNIQUE,
    `url` VARCHAR(200),
    `name` VARCHAR(200) UNIQUE,
    `nutrition_grades` VARCHAR(1),
    `category_id`INT UNSIGNED,
    `substitute_id` INT UNSIGNED,
    CONSTRAINT `fk_product_category`
        FOREIGN KEY (category_id) REFERENCES category(id)
        ON DELETE CASCADE,
    CONSTRAINT `fk_product_substitute`
        FOREIGN KEY (substitute_id) REFERENCES product(id)
        ON DELETE SET NULL
)ENGINE=InnoDB;
"""
import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'loff',
    'password': 'loff',
    'db': 'loff',
    'charset': 'utf8',
    'autocommit': False
}

CONF = {
    'host': DB_CONFIG['host'],
    'user': DB_CONFIG['user'],
    'db': DB_CONFIG['db'],
    'password': DB_CONFIG['password'],
    'charset': DB_CONFIG['charset'],
    'cursorclass': pymysql.cursors.DictCursor
}

REQUEST_LIST = [
    """INSERT INTO category (`name`) VALUES ('farces')""",
    """INSERT INTO product (`name`, `code`, `url`, `nutrition_grades`, \
`category_id`) SELECT "Farce de Veau", "3384480023221",
\"https://fr.openfoodfacts.org/produit/3384480023221/farce-de-veau-tendriade", \
"e", id AS category_id FROM category WHERE name = "farces";""",
    """INSERT INTO product (`name`, `code`, `url`, `nutrition_grades`, \
`category_id`) SELECT "Chair à saucisse Pur Porc", "3222472948438", \
"https://fr.openfoodfacts.org/produit/3222472948438/chair-a-saucisse-pur-porc-casino", \
"d", id AS category_id FROM category WHERE name = "farces";""",
    """INSERT INTO product (`name`, `code`, `url`, `nutrition_grades`, \
`category_id`) SELECT "Farce à Légumes, Pur Porc", "3254560320666", \
"https://fr.openfoodfacts.org/produit/3254560320666/farce-a-legumes-pur-porc-l-oiseau", \
"d", id AS category_id FROM category WHERE name = "farces";""",
    """SELECT c.name AS Category, p.code, p.name AS Product, \
p.nutrition_grades AS Nutriscore FROM category AS c \
LEFT JOIN product AS p ON c.id = p.category_id""",
]

CNX = pymysql.connect(**CONF)
CURSOR = CNX.cursor()

for idx, sql in enumerate(REQUEST_LIST):
    CURSOR.execute(sql)
    results = CURSOR.fetchall()
    print("\n{}. [{}…] Rows affected: {}".format(idx, sql[87:100], CURSOR.rowcount))

# CNX.commit()
CURSOR.close()
CNX.close()
