from Figure import Figure


class Square(Figure):
    def __init__(self, square_side: int):
        self.name = 'Square'
        self.square_side = square_side

    @property
    def area(self) -> int:
        return self.square_side ** 2

    @property
    def perimeter(self) -> int:
        return self.square_side * 4
