#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

def pig_latinify(word):
    """
    Describe your function
    #testing

    :param :
    :return:
    :raises:

    """
    vowels = ["a","e","i","o","u","y"]
    word = word.lower()
    for letter in vowels:
        if word[0] == letter:
            return word + "yay"
    else:
        for letter in vowels:
            for let in word:
                if letter == let:
                    i = word.index(let)
                    return word[i:]+word[:i]+"ay"

