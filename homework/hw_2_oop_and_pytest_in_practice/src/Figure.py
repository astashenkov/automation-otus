from typing import Union


class Figure:
    def add_area(self, figure) -> Union[int, float]:
        return round(self.area + figure.area, 2)
