#!/usr/bin/python3
"""Module for safe_function function."""
import sys


def safe_function(fct, *args):
    """Execute a function safely.

    Args:
        fct: Pointer to a function
        *args: Arguments for the function

    Returns:
        The result of the function, None otherwise
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
