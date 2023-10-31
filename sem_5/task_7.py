# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».
def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return number == 2
    delimiter = 3
    
    while delimiter * delimiter <= number and number % delimiter != 0:
            delimiter += 2
    return delimiter * delimiter > number

def gen_primes(limit: int) -> int:
    count = 0
    i = 2

    while count < limit:
        if is_prime(i):
            count += 1
            yield i
        i += 1



primes = gen_primes(100)

for number in primes:
    print(number, end=' ')