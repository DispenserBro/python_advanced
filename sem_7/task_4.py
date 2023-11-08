# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


from random import randint, choices, randbytes
from string import ascii_letters
import os
import os.path


def create_filename(min_len: int = 6, max_len: int = 30) -> str:
    
    filename_len = randint(min_len, max_len)
    
    return ''.join(choices(ascii_letters, k = filename_len))


def create_inner_file(min_bytes: int = 256, max_bytes: int = 4096):
    
    file_bytes = randint(min_bytes, max_bytes)
    
    return randbytes(file_bytes)


def create_files(directory: str, files_ext: str = 'txt', files_count = 42, min_len = 6, max_len = 30,
                 min_bytes = 256, max_bytes = 4096):

    for _ in range(files_count):
        filename = '.'.join((create_filename(min_len, max_len), files_ext))

        if not os.path.exists(filename):
            with open(os.path.join(filename), 'wb') as f:
                f.write(create_inner_file(min_bytes, max_bytes))



def create_files_with_variable_exts(files_with_exts: dict[str, int],
                                    directory: str = 'test_directory'):
    if os.path.isdir(directory):
        os.chdir(directory)
    else:
        os.mkdir(directory)
        os.chdir(directory)
    
    for file_ext, files_cnt in files_with_exts.items():
        create_files(directory, file_ext, files_cnt)

# create_files('12', 5)
# create_files_with_variable_exts({
#     'txt': 10,
#     '12': 2,
#     'ini': 5
# })


create_files_with_variable_exts({
    'txt': 10,
    '12': 2,
    'ini': 5
}, 'texts')
