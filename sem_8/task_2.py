# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import os.path
import json

from task_1 import BASE_DIR, Path


def check_access_level(level: int):
    if 0 < level < 8:
        return True


def check_pid(file_data: dict[int, dict], pid: int) -> bool:
    list_pids = []
    for el in file_data.values():
        for pid in el:
            list_pids.append(int(pid))
    print(list_pids)
    return pid not in list_pids


def write_json_data(file_data : dict[int, dict], name: str,
                    pid: int, access_level : int, filename : str = 'names.json'):

    if file_data.get(access_level, None) is None:
        file_data[access_level] = {}

    if not check_access_level(access_level):
        print('Уровень доступа должен быть в границах [1, 7]')
        return
    
    if check_pid(file_data, pid):
        file_data[access_level][pid] = name
    else:
        print('Такй pid уже есть в системе! Выберите другой')
        return
    
    with open(os.path.join(BASE_DIR, filename), 'w', encoding='utf-8') as f:
        json.dump(file_data, f, indent=2, ensure_ascii=False)


def get_file_data(filename: str = 'names.json') -> dict:
    with open(os.path.join(BASE_DIR, filename), 'r', encoding='utf-8') as f:
        file_data = json.load(f)
    print(file_data)
    return dict(file_data)


def loop_input(filename: str = 'names.json'):
    while True:
        if Path(os.path.join(BASE_DIR, filename)).exists():
            file_data = get_file_data(filename)
        else:
            # file_data = {i: {} for i in range(1, 8)}
            file_data = {}

        in_data = input('Введите имя, pid и уровень доступа через пробел:')

        if not in_data:
            break
    
        in_data = map(lambda x: int(x) if x.isdigit() else x, in_data.split())
        
        write_json_data(file_data, *in_data, filename)


if __name__ == "__main__":
    loop_input()