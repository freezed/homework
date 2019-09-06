#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
format syntax with tuple
https://stackoverflow.com/q/48990106/6709630
"""

t = ("alpha", "omega")
v = "to"

m = "From {} {} {} "
ms = "From {0} to {1}"
msg = "From {0} {var} {1} "

expr_list = [
    "t, v",
    "m.format(t, v)",
    "m.format(*t, v)",
    "ms.format(t)",
    "msg.format(t, v)",
    "msg.format(t, var=v)",
    "msg.format(*t, var=v)",
]

for num, expr in enumerate(expr_list):
    try:
        print("Expr{}, <{}>: «{}»".format(num, expr, eval(expr)))
    except Exception as except_detail:
        print("Expr{}, <{}> : Exception «{}»".format(num, expr, except_detail))
