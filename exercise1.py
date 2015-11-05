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
    This function will take a word as an argument and return it as the Pig Latin version of that word. If the first
    letter is a vowel the word will be returned with "yay" on the end of the word. If the first word is not a vowel
    then the letters of the word will be returned with the letters up to the first vowel in the word on the end
    followed by "ay"

    :param : Takes a string as input
    :return: A string in pig latin form

    """

    # list of vowels used to compare to the letters input
    vowels = ["a","e","i","o","u"]
    index = 0
    # these variable assignments ensure proper input and error checks
    word = str(word)
    word = word.lower()

    for letter in word:
        if word[0] in vowels:
            return word + "yay"
        else:
            # iterates through word with an index counter
            try:
                index += + 1
                if word[index] in vowels:
                    return word[index:] + word[:index] + "ay"
            # will ensure proper output if input is single consonant
            except IndexError:
                return word + "ay"
