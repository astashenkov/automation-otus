from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a_side: int, b_side: int):
        self.name = 'Rectangle'
        self.a_side = a_side
        self.b_side = b_side

    @property
    def area(self) -> int:
        return self.a_side * self.b_side

    @property
    def perimeter(self) -> int:
        return (self.a_side + self.b_side) * 2
