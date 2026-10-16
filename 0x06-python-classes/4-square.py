#!/usr/bin/python3
"""Module for Square class with property getter and setter."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
