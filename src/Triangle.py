import math

from Figure import Figure


def check_is_can_create_triangle(a_side: int, b_side: int, c_side: int):
    if not (a_side + b_side > c_side and a_side + c_side > b_side and c_side + b_side > a_side):
        raise ValueError(f'Unable to create a triangle with sides: {a_side}, {b_side}, {c_side}')


class Triangle(Figure):
    def __init__(self, a_side: int, b_side: int, c_side: int):
        check_is_can_create_triangle(a_side, b_side, c_side)
        self.name = 'Triangle'
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    @property
    def area(self) -> float:
        half_per = self.perimeter / 2
        return round(
            math.sqrt(
                half_per * (half_per - self.a_side) * (half_per - self.b_side) * (half_per - self.c_side)
            ), 2
        )

    @property
    def perimeter(self) -> int:
        return self.a_side + self.b_side + self.c_side
