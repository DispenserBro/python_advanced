from fractions import Fraction


frac1 = "3/7"
frac2 = "1/1"

frac_1 = list(map(int, frac1.split("/")))
frac_2 = list(map(int, frac2.split("/")))

sum_variants = [(frac_1[0] + frac_2[0], frac_1[0]),
                (frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1], frac_1[1] * frac_2[1])]

sum_variants = [(str(inner) for inner in el) for el in sum_variants]

sum_fracs = "/".join(sum_variants[frac_1[1] != frac_2[1]])
mul_fracs = "/".join((str(frac_1[0] * frac_2[0]), str(frac_1[1] * frac_2[1])))

print("Сумма дробей:", sum_fracs)
print("Произведение дробей:", mul_fracs)

fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")