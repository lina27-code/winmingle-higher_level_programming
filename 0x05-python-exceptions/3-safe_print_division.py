#!/usr/bin/python3
"""Module for safe_print_division function."""


def safe_print_division(a, b):
    """Divide 2 integers and print the result.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The value of the division, None otherwise
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
