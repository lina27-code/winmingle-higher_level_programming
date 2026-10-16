#!/usr/bin/python3
"""Module for safe_print_integer function."""


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value: The value to check and print

    Returns:
        True if value is an integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
