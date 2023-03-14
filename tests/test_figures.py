import math
import os
import sys

import pytest

sys.path.insert(1, os.path.join(sys.path[0], '../src/'))
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Square import Square


class TestFigures:
    triangle = Triangle(3, 5, 7)
    circle = Circle(10)
    rectangle = Rectangle(3, 6)
    square = Square(5)

    expected_triangle_perimeter = triangle.a_side + triangle.b_side + triangle.c_side
    half_triangle_perimeter = expected_triangle_perimeter / 2
    expected_triangle_area = round(
        math.sqrt(
            half_triangle_perimeter *
            (half_triangle_perimeter - triangle.a_side) *
            (half_triangle_perimeter - triangle.b_side) *
            (half_triangle_perimeter - triangle.c_side)
        ),
        2)

    expected_circle_area = round(math.pi * circle.radius * circle.radius, 2)
    expected_circle_perimeter = round(2 * math.pi * circle.radius, 2)

    expected_rectangle_area = (rectangle.a_side + rectangle.b_side) * 2
    expected_rectangle_perimeter = rectangle.a_side * rectangle.b_side

    expected_square_area = square.square_side ** 2
    expected_square_perimeter = square.square_side * 4

    def test_square_properties(self):
        assert self.square.name == 'Square', \
            f'Wrong name. Should be "Square", but {self.square.name}'
        assert self.square.perimeter == self.expected_square_perimeter, \
            f'Wrong square perimeter. Should be {self.expected_square_perimeter}, but {self.square.perimeter}'
        assert self.square.area == self.expected_square_area, \
            f'Wrong square area. Should be {self.expected_square_area}, but {self.square.area}'
        assert self.square.add_area(self.triangle) == round(self.expected_square_area + self.expected_triangle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_square_area + self.expected_triangle_area, 2)}, ' \
            f'but {self.square.add_area(self.triangle)}'
        assert self.square.add_area(self.circle) == round(self.expected_square_area + self.expected_circle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_square_area + self.expected_circle_area, 2)}, ' \
            f'but {self.square.add_area(self.circle)}'
        assert self.square.add_area(self.rectangle) == round(self.expected_square_area + self.expected_rectangle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_square_area + self.expected_rectangle_area, 2)}, ' \
            f'but {self.square.add_area(self.rectangle)}'

    def test_circle_properties(self):
        assert self.circle.name == 'Circle', \
            f'Wrong name. Should be "Circle", but {self.circle.name}'
        assert self.circle.perimeter == self.expected_circle_perimeter, \
            f'Wrong circle perimeter. Should be {self.expected_circle_perimeter}, but {self.circle.perimeter}'
        assert self.circle.area == self.expected_circle_area, \
            f'Wrong circle area. Should be {self.expected_circle_area}, but {self.circle.area}'
        assert self.circle.add_area(self.triangle) == round(self.expected_circle_area + self.expected_triangle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_circle_area + self.expected_triangle_area, 2)}, ' \
            f'but {self.circle.add_area(self.triangle)}'
        assert self.circle.add_area(self.square) == round(self.expected_circle_area + self.expected_square_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_circle_area + self.expected_square_area, 2)}, ' \
            f'but {self.circle.add_area(self.square)}'
        assert self.circle.add_area(self.rectangle) == round(self.expected_circle_area + self.expected_rectangle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_circle_area + self.expected_rectangle_area, 2)}, ' \
            f'but {self.circle.add_area(self.rectangle)}'

    def test_rectangle_properties(self):
        assert self.rectangle.name == 'Rectangle', \
            'Wrong name. Should be "Rectangle", but {self.rectangle.name}'
        assert self.rectangle.perimeter == self.expected_rectangle_perimeter, \
            f'Wrong rectangle perimeter. Should be {self.expected_rectangle_perimeter}, but {self.rectangle.perimeter}'
        assert self.rectangle.area == self.expected_rectangle_area, \
            f'Wrong rectangle area. Should be {self.expected_rectangle_area}, but {self.rectangle.area}'
        assert self.rectangle.add_area(self.triangle) == round(self.expected_rectangle_area + self.expected_triangle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_rectangle_area + self.expected_triangle_area, 2)}, ' \
            f'but {self.rectangle.add_area(self.triangle)}'
        assert self.rectangle.add_area(self.circle) == round(self.expected_rectangle_area + self.expected_circle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_rectangle_area + self.expected_circle_area, 2)}, ' \
            f'but {self.rectangle.add_area(self.circle)}'
        assert self.rectangle.add_area(self.square) == round(self.expected_rectangle_area + self.expected_square_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_rectangle_area + self.expected_square_area, 2)}, ' \
            f'but {self.rectangle.add_area(self.square)}'

    def test_triangle_properties(self):
        assert self.triangle.name == 'Triangle', \
            f'Wrong name. Should be "Triangle", but {self.triangle.name}'
        assert self.triangle.perimeter == self.expected_triangle_perimeter, \
            f'Wrong triangle perimeter. Should be {self.expected_triangle_perimeter}, but {self.triangle.perimeter}'
        assert self.triangle.area == self.expected_triangle_area, \
            f'Wrong triangle area. Should be {self.expected_triangle_area}, but {self.triangle.area}'
        assert self.triangle.add_area(self.square) == round(self.expected_triangle_area + self.expected_square_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_triangle_area + self.expected_square_area, 2)}, ' \
            f'but {self.triangle.add_area(self.square)}'
        assert self.triangle.add_area(self.circle) == round(self.expected_triangle_area + self.expected_circle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_triangle_area + self.expected_circle_area, 2)}, ' \
            f'but {self.triangle.add_area(self.circle)}'
        assert self.triangle.add_area(self.rectangle) == round(self.expected_triangle_area + self.expected_rectangle_area, 2), \
            f'Wrong summ of areas. Should be {round(self.expected_triangle_area + self.expected_rectangle_area, 2)}, ' \
            f'but {self.triangle.add_area(self.rectangle)}'

    @pytest.mark.xfail
    def test_create_triangle(self):
        Triangle(1, 1, 66)
