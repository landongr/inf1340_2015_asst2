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
    Test find function when substring is not found within sliced string.
    """
    assert find("This is an ex-parrot", "parrt", 0, 20) == -1

def test_outside_substring():
    """
    Test find function for when substring is outside of sliced string.
    """
    assert find("atcgcgcatagcgtagactagcgtactgactgactgactgac","cata", 16 , 20) == -1

def test_substring_not_fully_inside():
    """
    Test find function for when a part of the substring is in sliced string.
    """
    assert find("atcgcgcatagcgtagactagcgtactgactgactgactgac","catagcgt", 5, 10) == -1

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

def test_multi_find_basic_2():
    """
    Test multi_find function when substring[s] are not found.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "ii", 0, 20) == "0"

def test_substring_not_fully_inside_2():
    """
    Test multi_find function for when a part of a substring is in sliced string.
    """
    assert find("agtcgcgcatcgcgtagactagcgtactgactgactgactgac","tcg", 0, 10) == 2