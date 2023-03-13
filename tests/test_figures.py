import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../src/'))
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Square import Square


class TestFigures:
    triangle = Triangle(3, 5, 6) # 7.48
    circle = Circle(10) # 314
    rectangle = Rectangle(3, 6) # 18
    square = Square(5) # 25

    def test_square_properties(self):
        assert self.square.name == 'Square', f'Wrong name. Should be "Square", but {self.square.name}'
        assert self.square.perimeter == 20, f'Wrong square perimeter. Should be 20, but {self.square.perimeter}'
        assert self.square.area == 25, f'Wrong square area. Should be 25, but {self.square.area}'
        assert self.square.add_area(self.triangle) == 32.48, f'Wrong summ of areas. Should be 32.48, but {self.square.add_area(self.triangle)}'
        assert self.square.add_area(self.circle) == 339.16, f'Wrong summ of areas. Should be 339.16, but {self.square.add_area(self.circle)}'
        assert self.square.add_area(self.rectangle) == 43, f'Wrong summ of areas. Should be 43, but {self.square.add_area(self.rectangle)}'

    def test_circle_properties(self):
        assert self.circle.name == 'Circle', f'Wrong name. Should be "Circle", but {self.circle.name}'
        assert self.circle.perimeter == 62.83, f'Wrong circle perimeter. Should be 62.83, but {self.circle.perimeter}'
        assert self.circle.area == 314.16, f'Wrong circle area. Should be 314.16, but {self.circle.area}'
        assert self.circle.add_area(self.triangle) == 321.64, f'Wrong summ of areas. Should be 321.64, but {self.circle.add_area(self.triangle)}'
        assert self.circle.add_area(self.square) == 339.16, f'Wrong summ of areas. Should be 339.16, but {self.circle.add_area(self.square)}'
        assert self.circle.add_area(self.rectangle) == 332.16, f'Wrong summ of areas. Should be 332.16, but {self.circle.add_area(self.rectangle)}'

    def test_rectangle_properties(self):
        assert self.rectangle.name == 'Rectangle', f'Wrong name. Should be "Rectangle", but {self.rectangle.name}'
        assert self.rectangle.perimeter == 18, f'Wrong rectangle perimeter. Should be 18, but {self.rectangle.perimeter}'
        assert self.rectangle.area == 18, f'Wrong rectangle area. Should be 18, but {self.rectangle.area}'
        assert self.rectangle.add_area(self.triangle) == 25.48, f'Wrong summ of areas. Should be 25.48, but {self.rectangle.add_area(self.triangle)}'
        assert self.rectangle.add_area(self.circle) == 332.16, f'Wrong summ of areas. Should be 332.16, but {self.rectangle.add_area(self.circle)}'
        assert self.rectangle.add_area(self.square) == 43, f'Wrong summ of areas. Should be 43, but {self.rectangle.add_area(self.square)}'

    def test_triangle_properties(self):
        assert self.triangle.name == 'Triangle', f'Wrong name. Should be "Triangle", but {self.triangle.name}'
        assert self.triangle.perimeter == 14, f'Wrong triangle perimeter. Should be 14, but {self.triangle.perimeter}'
        assert self.triangle.area == 7.48, f'Wrong triangle area. Should be 7.48, but {self.triangle.area}'
        assert self.triangle.add_area(self.square) == 32.48, f'Wrong summ of areas. Should be 32.48, but {self.triangle.add_area(self.square)}'
        assert self.triangle.add_area(self.circle) == 321.64, f'Wrong summ of areas. Should be 321.64, but {self.triangle.add_area(self.circle)}'
        assert self.triangle.add_area(self.rectangle) == 25.48, f'Wrong summ of areas. Should be 25.48, but {self.triangle.add_area(self.rectangle)}'
