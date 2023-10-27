# ✔Создайте вручную кортеж содержащий элементы разных типов.
# ✔Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

tuple_1 = ("`123123", "ewfsdf", 123, 23.0, [123], [])

types_dict = {}

for el in tuple_1:
    if type(el) in types_dict:
        types_dict[type(el)] += [el]
    else:
        types_dict[type(el)] = [el]

print(types_dict)
