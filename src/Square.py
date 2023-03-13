from Figure import Figure


class Square(Figure):
    def __init__(self, square_side):
        self.name = 'Square'
        self.square_side = square_side

    @property
    def area(self):
        return self.square_side ** 2

    @property
    def perimeter(self):
        return self.square_side * 4
