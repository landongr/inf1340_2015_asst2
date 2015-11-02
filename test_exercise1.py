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

    # Test string with more than one vowel in string
    assert pig_latinify("constantinople") == "onstantinoplecay"

    # Test string with capital letters
    assert pig_latinify("CaPiTaL") == "apitalcay"

    # Test one letter string
    assert pig_latinify("a") == "ayay"

    # Test empty string
    assert pig_latinify("") == "Error please use a valid word"

    # Test string with non-letters
    assert pig_latinify("dollar$") == "Error please use a valid word"

    # Test with integer input
    assert pig_latinify(3) == "Error please use a valid word"

    # Test for whitespace in sting
    assert pig_latinify("white space") == "Error please use a valid word"

