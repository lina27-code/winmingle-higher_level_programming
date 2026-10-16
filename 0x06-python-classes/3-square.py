#!/usr/bin/python3
"""Module for Square class with area method."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
