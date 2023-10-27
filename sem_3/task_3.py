# ✔Создайте вручную список с повторяющимися элементами.
# ✔Удалите из него все элементы, которые встречаются дважды.
from random import randint


lst1 = []

for i in range(20):
    lst1.append(randint(0, 10))

print(lst1)

i = 0

while i < len(lst1):
    if lst1.count(lst1[i]) > 2:
        el = lst1[i]
        lst1.remove(el)
        lst1.remove(el)
        continue
    i += 1

print(lst1)