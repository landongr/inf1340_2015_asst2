#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

def user_input():
    """
    This function checks to make sure user input is legal
    and returns legal user input to the pig latin function
    """
    word = raw_input("Enter your word!")
    while word.isalpha() == False:
        print "Please enter a single word"
        word = raw_input("Enter your word!")
    else:
        return word.lower()

def pig_latinify():
    """
    Describe your function
    #testing

    :param :
    :return:
    :raises:

    """
    vowels = ["a","e","i","o","u","y"]
    word = user_input()

    while True:
        for letter in vowels:
            if word[0] == letter:
                print word + "yay"
                return False
        else:
            for letter in vowels:
                for let in word:
                    if letter == let:
                        i = word.index(let)
                        print word[i:]+word[:i]+"ay"
                        return False

pig_latinify()

