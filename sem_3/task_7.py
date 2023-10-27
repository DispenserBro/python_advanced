# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends_dict = {
    "Паша":('котелок','нож','еда','одеяло'),
    "Ваня":('котелок','нож','мяч','топор'),
    "Игорь":('котелок','вода','еда','топор'),
    "Коля": ('котелок', 'еда', 'нож', 'топор', 'компас'),
}

print(friends_dict)
unique_things = []
except_one_things = []
things_set = set()

for things_tuple in friends_dict.values():
    things_set.update(things_tuple)

print(things_set)

for el in things_set:
    thing_count = 0
    for friend in friends_dict:
        if el in friends_dict[friend]: 
            thing_count += 1
        if thing_count == len(friends_dict) - 1 and friend == tuple(friends_dict.keys())[-1]:
            except_one_things.append(el)
        elif thing_count == 1 and friend == tuple(friends_dict.keys())[-1]:
            unique_things.append(el)

print(f"{unique_things = }")
print(f"{except_one_things = }")

for el in unique_things:
    for friend in friends_dict:
        if el in friends_dict[friend]:
            print(f"{el} есть только у {friend}")

for el in except_one_things:
    for friend in friends_dict:
        if el not in friends_dict[friend]:
            print(f"У {friend} нет {el}")

