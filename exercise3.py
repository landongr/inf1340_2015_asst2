#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

table_1 = [["Number", "Surname", "Ages"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

table_2 = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]


def schema_check(table1, table2):
    """
    This function takes two tables as input and ensures that they have the same schema, which in this
    case means that the title of each column is exactly the same and each table has the same number of columns
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: None
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema

    """

    # compares the first row of each table to ensure the titles and number of columns match
    if table1[0] != table2[0]:
        raise MismatchedAttributesException


def union(table1, table2):
    """

    Combines input tables and returns a table that contains all unique rows that appear in either input tables

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: a table with all unique rows from either input tables
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema
    """

    schema_check(table1, table2)
    # combines the two input tables, then removes the duplicates from the combined table
    union_table = table1 + table2
    return remove_duplicates(union_table)




def intersection(table1, table2):
    """
    Combines input tables and returns a table that contains all unique rows that appear in both input tables

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: a table with all unique rows from both input tables
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema

    """

    schema_check(table1, table2)
    intersection_list = []
    # iterates through rows in table one and table two
    for lists1 in table1:
        for lists2 in table2:
            # compares rows between the two tables and appends matching rows to the empty list
            if lists1 == lists2:
                intersection_list.append(lists1)
    return intersection_list




def difference(table1, table2):
    """
    Combines input tables and returns a table that contains all unique rows that appear in
    the first input table but not the second as well as the title row.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: a table with all unique rows from the first input table and the title row
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same schema

    """

    schema_check(table1, table2)
    # pulls column titles from table one for input in the final table
    column_titles = table1[0]
    count = 0
    while count < len(table1):
        # iterates though rows in each table
        for lists1 in table1:
            for lists2 in table2:
                # compares rows and removes matching rows from table one
                if lists1 == lists2:
                    table1.remove(lists1)
        count += + 1
    # inserts column titles as top row and returns the final table
    table1.insert(0,column_titles)
    return table1


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """

    pass

GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

#schema_check(GRADUATES, MANAGERS)
#union(table_1, table_2)
#intersection(table_1, table_2)
#difference(table_1, table_2)
