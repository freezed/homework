#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author:
https://openclassrooms.com/forum/sujet/exercices-du-cours-python-postez-ici?page=25#message-92220709
"""
from os import system
import subprocess


print("$ AFIGO")
input("Check ENTREE for scan dhcp")
system("clear")
print("")
print("IP LIST")
print("------------------------------------------------------------")
print("")
for i in range(0, 255):
  a = subprocess.getoutput("host 192.168.1."+str(i))
  if a == (str(i)+".1.168.192.in-addr.arpa has no PTR record"):
    pass
  else:
    print(a)
    pass
print("")
print("------------------------------------------------------------")