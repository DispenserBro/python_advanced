# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def get_unicode_dict(id_pair: str) -> dict[str, int]:
    id_1, id_2 = sorted(map(int, id_pair.split()))
    unicode_dict = {}
    
    for cur_id in range(id_1, id_2 + 1):
        unicode_dict[chr(cur_id)] = cur_id
    
    return unicode_dict

print(get_unicode_dict('1100 1000'))