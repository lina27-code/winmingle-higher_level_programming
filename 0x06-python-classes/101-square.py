#!/usr/bin/python3
"""Module for Square class with __str__ method."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position of the square (default (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters with position."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            The square as a string.
        """
        if self.__size == 0:
            return ""

        lines = []
        for i in range(self.__position[1]):
            lines.append("")

        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
