#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        *args: Arguments to pass to the function.

    Returns:
        The result of the function, or None if an exception occurs.
    """
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        return None
