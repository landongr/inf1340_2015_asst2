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
    This function will take a word as an argument and return it as the Pig Latin
    version of that word.

    :param : Will take a  word as input
    :return: Will output word as a string in its Pig Lain form. If the first
    letter is a vowel the word will be returned with "yay" on the end of the word.
    If the first word is not a vowel then the letters of the word will be returned
    with the letters up to the first vowel in the word on the end followed by "ay"
    :raises: "Please use a valid word" raised if input is not alphabetic characters
    or input is an empty string.

    """

    # list of vowels used to compare to the letters input
    vowels = ["a","e","i","o","u","y"]
    # index counter used to iterate though the letter input
    index = 0
    # these variable assignments ensure proper input and error checks
    word = str(word)
    word = word.lower()
    # check for proper input
    if word.isalpha() and len(word) > 0:
        # iterate through word and check if first letter is vowel
        for letter in word:
            if word[0] in vowels:
                return word + "yay"
            else:
                # iterates though word with an index counter
                index += + 1
                # checks for vowels inside the word
                if word[index] in vowels:
                    return word[index:] + word[:index] + "ay"
    else:
        # error message returned if input is not valid
        return "Error please use a valid word"


