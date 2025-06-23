import math

class Shape:
    """A base class for shapes, intended to be inherited from."""
    def area(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Shape):
    """A rectangle shape that calculates its area."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides the base method to return the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """A circle shape that calculates its area."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides the base method to return the area of the circle."""
        return math.pi * (self.radius ** 2)
