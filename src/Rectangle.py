from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.name = 'Rectangle'
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2
