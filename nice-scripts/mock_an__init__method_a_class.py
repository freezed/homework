#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
source : https://medium.com/@george.shuklin/mocking-complicated-init-in-python-6ef9850dd202
"""


class Compl(object):
    def __init__(self, arg1, arg2):
        self.var1 = complicated_to_mock(arg1)
        self.var2 = self.var2.complicated_to_mocK2(arg2)

        if self.var1 in self.var2 and self.var1 != self.var2:
            self.var3 = self.var2 - self.var1 + ctm3(ctm4())

        self.foo  = {
            "1": {"price": "2.7", "quantity": "10"},
            "2": {"price": "8.0", "quantity": "2"},
        }

    def simple(self, arg3):
        if arg3 > self.var1:
            return None
        else:
            return arg3 - self.var1


from unittest.mock import patch

def test_simple_none():
    with patch.object(Compl, "__init__", lambda x, y, z: None):
        c = Compl(None, None)
        c.var1 = 0
        c.foo = {"foo":"bar", "FOO":"BAR"}
        assert c.simple(1) is None
        assert [i for i in c.foo.keys()] == ["foo", "FOO"]

def test_simple_substraction():
    with patch.object(Compl, "__init__", lambda x, y, z: None):
        c = Compl(None, None)
        c.var1 = 1
        assert c.simple(1) == 0
