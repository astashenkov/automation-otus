import math
from Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.name = 'Triangle'
        if a + b > c and a + c > b and c + b > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError('Unable to create a triangle')

    @property
    def area(self):
        half_per = self.perimeter / 2
        return round(
            math.sqrt(
                half_per * (half_per - self.a) * (half_per - self.b) * (half_per - self.c)
            ), 2
        )

    @property
    def perimeter(self):
        return self.a + self.b + self.c
