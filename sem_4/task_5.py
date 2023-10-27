# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

def calculate_salary_bonus(employee: list[str], salary: list[int],
                           bonus_percents: list[int]) -> dict[str, float]:
    bonus_dict = {}
    
    for i in range(len(salary)):
        bonus = salary[i] * (float(bonus_percents[i][:-1]) / 100)
        bonus_dict[employee[i]] = bonus
    return bonus_dict

name = ['Иван', 'Павел', 'Сергей']
stavka = [100000, 150000, 200000]
pr = ['10.25%', '12.2%', '13.8%']

print(calculate_salary_bonus(name, stavka, pr))