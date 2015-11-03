#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

def test_find_basic_2():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrt", 0, 20) == -1

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

def test_multi_find_basic_2():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "ii", 0, 20) == "0"

def test_outside_substring():
    #
    assert find("atcgcgcatagcgtagactagcgtactgactgactgactgac","cata", 16 , 20) == -1

try:
   find("This is an ex-parrot", parrot, 0, 20)
except NameError:
   assert True

try:
   find("This is an ex-parrot", "parrot")
except TypeError:
   assert True

try:
   multi_find("Ni! Ni! Ni! Ni!", "Ni", 3.3, 20)
except TypeError:
   assert True


