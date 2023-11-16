# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_circumference(self) -> float:
        return self.radius * 2 * pi

    def get_area(self) -> float:
        return self.get_circumference() ** 2 / (4 * pi)


print(Circle(1).get_area())
