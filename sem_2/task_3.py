# ✔Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔Диаметр не превышает 1000 у.е.
# ✔Точность вычислений должна составлять не менее 42 знаков после запятой.

from math import pi
from decimal import Decimal, getcontext

getcontext().prec = 42

diameter = Decimal(input("Enter diameter: "))

S = Decimal(pi * (diameter / 2.0) ** 2)
