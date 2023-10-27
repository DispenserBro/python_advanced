# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sum_between(in_lst: list[int], idx_1: int, idx_2: int) -> int:
    idx_1, idx_2 = sorted((idx_2, idx_1))
    # idx_1 = idx_1 if idx_1 >= 0 else 0
    # idx_2 = idx_2 if idx_2 <= len(in_lst) else len(in_lst) - 1

    # return sum([in_lst[i] for i in range(idx_1, idx_2 + 1)])
    return sum(in_lst[idx_1 : idx_2 + 1])

lst = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13]
print(sum_between(lst, 20, -7))
print(sum(lst))