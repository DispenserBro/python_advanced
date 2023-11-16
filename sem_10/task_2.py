# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, length: float, width: float = None):
        self.length = length
        self.width = width if width is not None else length

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width


rect1 = Rectangle(2, 4)
square1 = Rectangle(4)

print(rect1.get_perimeter())
print(square1.get_perimeter())