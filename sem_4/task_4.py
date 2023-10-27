# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.

def bubble_sort(in_lst: list[int]) -> None:
    lst_len = len(in_lst)

    for i in range(lst_len - 1):
        for j in range(lst_len - i - 1):
            if in_lst[j] > in_lst[j + 1]:
                in_lst[j], in_lst[j + 1] = in_lst[j + 1], in_lst[j]


print(lst := [11, 234, 456, 312, 0, 1, 5])
bubble_sort(lst)
print(lst)
