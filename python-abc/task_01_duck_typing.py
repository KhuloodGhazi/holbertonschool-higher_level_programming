#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """abstract class for shapes"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """circle"""

    def __init__(self, radius):
        """

        Args:
          radius: radius
        """
        self.radius = radius

    def area(self):
        """

        Return: area
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """

        Return: perimeter
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """rectangle"""

    def __init__(self, width, height):
        """

        Args:
           width: width
           height: height
        """
        self.width = width
        self.height = height

    def area(self):
        """

        Return: area
        """
        return self.width * self.height

    def perimeter(self):
        """

        Return: perimeter
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """information about shape
    Args:
      shape: shape object
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
