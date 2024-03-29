import math

from Figure import Figure


class Circle(Figure):
    def __init__(self, radius: int):
        self.name = 'Circle'
        self.radius = radius

    @property
    def area(self) -> float:
        try:
            return round(math.pi * abs(self.radius) ** 2, 2)
        except TypeError:
            print('Error: Unexpected value of the circle radius')

    @property
    def perimeter(self) -> float:
        try:
            return round(2 * math.pi * abs(self.radius), 2)
        except TypeError:
            print('Error: Unexpected value of the circle radius')
