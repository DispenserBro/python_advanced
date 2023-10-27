# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

letters = 'asfasd'
words = 'asd dg cvcxv'
text = 'ergever were'
s = 'letter s'

def change_variables_containers():
    for variable in globals():
        if variable.endswith('s') and len(variable) != 1:
            pass