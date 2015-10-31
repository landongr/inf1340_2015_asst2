#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

table_1 = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

table_2 = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

def table_service(table1, table2):
    if table1[0] != table2[0]:
        print MismatchedAttributesException
    count1 = 0
    count2 = 0
    while count1 < len(table1):
        if len(table1[count1]) == len(table1[0]):
            count1 += + 1
            continue
        else:
            print MismatchedAttributesException
            break
    while count2 < len(table2):
        if len(table2[count2]) == len(table2[0]):
            count2 += + 1
            continue
        else:
            print MismatchedAttributesException
            break



def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    #Return a new table that contains all uniuqe row

    table_service(table1, table2)
    union_table = table1 + table2
    return remove_duplicates(union_table)




def intersection(table1, table2):
    """
    Describe your function

    """
    table_service(table1, table2)
    intersection_list = []
    for lists1 in table1:
        for lists2 in table2:
            if lists1 == lists2:
                intersection_list.append(lists1)
    return intersection_list




def difference(table1, table2):
    """
    Describe your function

    """
    table_service(table1, table2)
    column_titles = table1[0]
    count = 0
    while count < len(table1):
        for lists1 in table1:
            for lists2 in table2:
                if lists1 == lists2:
                    table1.remove(lists1)
        count += + 1
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



#table_service(table_1, table_2)
#union(table_1, table_2)
#intersection(table_1, table_2)
#difference(table_1, table_2)