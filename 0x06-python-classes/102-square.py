#!/usr/bin/python3
"""Module for Square class with comparison operators."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int or float): The size of the square (default 0).
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
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square's area is less than the other's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square's area is less than or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square's area is greater than the other's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square's area is greater than or equal."""
        return self.area() >= other.area()
