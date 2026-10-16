#!/usr/bin/python3
"""Module for MagicClass class."""
import math


class MagicClass:
    """A class representing a magic circle."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int or float): The radius of the circle (default 0).

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Compute the area of the circle.

        Returns:
            The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Compute the circumference of the circle.

        Returns:
            The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
