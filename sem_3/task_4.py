# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.
from random import randint


lst1 = []

for i in range(20):
    lst1.append(randint(0, 10))

print(lst1)

lst2 = [i]