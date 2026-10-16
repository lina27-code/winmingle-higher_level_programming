#!/usr/bin/python3
"""Module for list_division function."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists.

    Args:
        my_list_1: First list
        my_list_2: Second list
        list_length: Number of elements to divide

    Returns:
        A new list with all divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (int, float)) or \
                    not isinstance(b, (int, float)):
                raise TypeError
            result = a / b
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
