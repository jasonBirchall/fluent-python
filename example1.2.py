"""
vector2d.py: a simplistic class demonstrating some special methods

It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__mul__`` methods.

This example is greatly expanded later in the book.

Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Absolute value::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Scalar multiplication::

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

"""

import math


class Vector:

    def __init__(self, x=0, y=0):
        """Create a vector, example: v = Vector(1,2)"""
        self.x = x
        self.y = y

    def __repr__(self):
        """
        The !r is used to get the repr() of the argument. This is important as the repr() of a string is the string itself.
        If you don't use !r, you'll end up in an infinite loop as repr() of string calls __repr__() of the object passed
        to it, which is again a string and so on.
        It allows the interpreter to display the vector in the console.
        """
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        """Returns the magnitude of the vector"""
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """Returns True if magnitude is not zero"""
        return bool(abs(self))

    def __add__(self, other):
        """Returns the vector addition of self and other"""
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """Returns the vector multiplied by a scalar"""
        return Vector(self.x * scalar, self.y * scalar)
