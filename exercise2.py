#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# (input_string, substring, start, end): <- you leave as a parameter and you test it in test cases, does not need to be called yet. Same as lab 3



def find(input_string, substring, start, end):

    """
    This function finds a sub-string within a longer string, both are put in as
    arguments within the function. The search can be initiated within a slice of
    the long string by providing start and end as the third and forth arguments
    in the function

    :param : the long string to be searched is the first argument, the substring to be
    found is the second argument and the third and forth arguments are the start and end
    of a slice of the long string to be searched.
    :return: an integer that indicates the index of the substring or a -1 if the substring
    is not present
    :raises:

    """
    substring_len = len(substring)
    cnt1 = 0
    cnt2 = substring_len
    # checks for substring in input string
    for letter in input_string[start:end]:
        slice_str = input_string[cnt1:cnt2]
        if substring == slice_str:
            return cnt1
        # shifts the sliced string 1 character to the right
        cnt1 += 1
        cnt2 = cnt1 + substring_len
    # if no matches are found, returns -1
    return -1




def multi_find(input_string, substring, start, end):
    """
    This function finds a sub-string within a longer string, both are put in as
    arguments within the function. The search can be initiated within a slice of
    the long string by providing start and end as the third and forth arguments
    in the function

    :param :the long string to be searched is the first argument, the substring to be
    found is the second argument and the third and forth arguments are the start and end
    of a slice of the long string to be searched.
    :return:a string that lists all indices of all locations where the substring if found, or a 0 if the substring
    is not present
    :raises:

    """

    substring_len = len(substring)
    cnt1 = 0
    cnt2 = substring_len
    result = ""
    # checks if substring is in input string
    for letters in input_string[start:end]:
        slice_str = input_string[cnt1:cnt2]
        if substring == slice_str:
            if result == "":
                result = str(cnt1)
            # placeholder for subsequent indices found
            else:
                result = result + "," + str(cnt1)
        # shifts the sliced string 1 character to the right
        cnt1 += 1
        cnt2 = cnt1 + substring_len
    # if result still equals to "", substring is not found and should return "0"
    if result == "":
        return "0"
    # otherwise, it will list all indices found
    else:
        return result


