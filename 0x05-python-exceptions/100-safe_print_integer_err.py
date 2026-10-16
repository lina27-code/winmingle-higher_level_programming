#!/usr/bin/python3
"""Module for safe_print_integer_err function."""
import sys


def safe_print_integer_err(value):
    """Print an integer with "{:d}".format().

    Args:
        value: The value to check and print

    Returns:
        True if value is an integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
