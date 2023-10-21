# ✔Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# ✔Используйте комплексные числа для извлечения квадратного корня.
a = float(input("Enter a coefficient: "))
b = float(input("Enter b coefficient: "))
c = float(input("Enter c coefficient: "))

discr = b ** 2 - 4 * a * c

if discr < 0:
    x1 = (-b + (discr * 1j ** 2) ** 0.5) / (2 * a)
    x2 = (-b + (discr * 1j ** 2) ** 0.5) / (2 * a)
elif discr > 0:
    x1 = (-b + (discr ** 0.5)) / (2 * a)
    x2 = (-b - (discr ** 0.5)) / (2 * a)
else:
    x1 = -b / (2 * a)
    x2 = x1

print(f"{x1=}, {x2=}")