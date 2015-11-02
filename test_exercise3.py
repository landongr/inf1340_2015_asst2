#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, schema_check, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

GRADUATES_WRONG = [["Number", "Surname", "DOB"],
             [7274, "Robinson", "01/03/93"],
             [7432, "O'Malley", "10/10/01"],
             [9824, "Darkes", "09/08/76"]]

MANAGERS_WRONG = [["Number", "Surname", "Age", "Sex"],
            [9297, "O'Malley", 56, "F"],
            [7432, "O'Malley", 39, "M"],
            [9824, "Darkes", 38, "M"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

def test_schema_check():
    """
    Test to make sure the schema check does or does not throw errors when appropriate
    """
    # Checks to ensure no error is thrown when schemas match
    assert schema_check(GRADUATES, MANAGERS) == None
    # Checks to ensure an error is thrown if the schema titles to not match
    assert schema_check(GRADUATES_WRONG, MANAGERS) == MismatchedAttributesException
    # Chckes to ensure an error is throw if the amount of columns of the table do not match
    assert schema_check(GRADUATES, MANAGERS_WRONG) == MismatchedAttributesException