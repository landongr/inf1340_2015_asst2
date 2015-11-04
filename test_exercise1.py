#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

def test_multiple_vowels():
    """
    Test string with more than one vowel in
    """
    assert pig_latinify("constantinople") == "onstantinoplecay"

def test_capital_letters():
    """
    Test string with capital letters
    """
    assert pig_latinify("CaPiTaL") == "apitalcay"

def test_one_letter_vowel():
    """
    Test one letter vowel string
    """
    assert pig_latinify("a") == "ayay"

def test_one_letter_consonant():
    """
    Test one letter consonant string
    """
    assert pig_latinify("h") == "hay"

