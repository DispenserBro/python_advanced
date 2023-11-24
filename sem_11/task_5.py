# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, width: float, height: float = None):
        self.width = width
        self.height = height if height is not None else width

    def _check_other(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Other object must be a Rectangle")

    def __add__(self, other: "Rectangle"):
        self._check_other(other)
        new_length = self.width + other.width
        new_width = self.height + other.height

        return Rectangle(new_length, new_width)

    def __sub__(self, other: "Rectangle"):
        self._check_other(other)
        if other.perimeter() <= self.perimeter():
            new_length = self.width - other.width
            new_width = self.height - other.height

            return Rectangle(new_length, new_width)

        raise ValueError("Other Rectangle must have less perimeter")

    def __lt__(self, other: 'Rectangle') -> bool:
        self._check_other(other)
        return self.area() < other.area()

    def __repr__(self) -> str:
        return f'Rectangle({self.width}, {self.height})'
    
    def __str__(self) -> str:
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


rect1 = Rectangle(2, 4)
square1 = Rectangle(4)

print(rect1.perimeter())
print(square1.perimeter())

# rect2 = rect1 - square1
# print(rect2.get_perimeter() == square1.get_perimeter() - rect1.get_perimeter())

print(rect1 > square1)
print(rect1 >= square1)
print(rect1 < square1)
print(rect1 <= square1)
print(rect1 == square1)
print(rect1 != square1)
