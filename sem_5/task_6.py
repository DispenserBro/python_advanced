# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

# lst_mul_1 = [i for i in range(2,10)]
# lst_mul_2 = [i for i in range(2,11)]

# for i in lst_mul_1:
#     for j in lst_mul_2:
#         print(f'{i}x{j}={i*j}')

# lst_equations = [f'{i: <2}x{j: > 2} = {i*j: >2}' for j in range(2,11) for i in range(2,10)]
# lst_table = ['\t'.join(lst_equations[i:i+4]) for i in range(0, len(lst_equations), 4)]
# lst_table = lst_table[::2] + lst_table[1::2]

# print(*lst_table, sep='\n')

# temp = '\n'
# lst_1 = [f'{j: >2} * {i: >2} = {i * j: >2} {temp * (j // 5)}' for i in
#        range(2, 11) for j in range(2, 6)]
# print(*lst_1)

print('\n\n'.join(['\n'.join(['\t'.join([f'{y} x {x} = {x*y:>2}' for y in range(2+k,6+k)]) for x in range(2,10)]) for k in [0,4]]))