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
    Describe your function

    :param :
    :return:
    :raises:

    """
    substring_len = len(substring)
    #start index for sliced comparison string
    cnt2 = 0
    #end index for sliced comparison string
    cnt3 = substring_len
    #for variable in the given index range
    for cnt1 in input_string[start:end]:
        #defining the sliced string for comparison
        slice_str = input_string[cnt2:cnt3]
        #compare substring with sliced string from input string
        if substring == slice_str:
            #index of the first character of the sliced string
            return cnt2
        #shifts the sliced string 1 character to the right for next loop
        cnt2 = cnt2 + 1
        cnt3 = cnt2 + substring_len
    #if no matches are found, returns -1
    return -1




def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    substring_len = len(substring)
    #start index for sliced comparison string
    cnt2 = 0
    #end index for sliced comparison string
    cnt3 = substring_len
    result = ""
    #for variable in the given index range
    for cnt1 in input_string[start:end]:
        #defining the sliced string for comparison
        slice_str = input_string[cnt2:cnt3]
        #compare substring with sliced string from input string
        if substring == slice_str:
            #for the first index found, the result should equal to "" for the first index found
            if result == "":
                #declaring result to be the first index in string form
                result = str(cnt2)
            #for subsequent indices after the first index found
            else:
                #the result should contain the new index found following the previous index/indices
                result = result + "," + str(cnt2)
        #shifts the sliced string 1 character to the right
        cnt2 = cnt2 + 1
        cnt3 = cnt2 + substring_len
    #if result is still equal to "", it means that substring is not found and should return "0"
    if result == "":
        return "0"
    #otherwise, it will list all indices found
    else:
        return result



