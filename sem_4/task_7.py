# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def is_all_profitable(companies: dict[str, list[int]]) -> bool:
    return any(sum(profit) < 0 for profit in companies.values())


companies = {
    'google': [100000, -10000, 23423450, -3453546],
    'nestle': [1000, 1234123, 154534, 34536],
    'amd': [1000, -14245345, -2353453]
}

print(is_all_profitable(companies))