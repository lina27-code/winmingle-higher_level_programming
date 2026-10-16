#!/usr/bin/python3
"""Module for safe_print_list_integers function."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list: The list to print elements from
        x: The number of elements to access in my_list

    Returns:
        The real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
