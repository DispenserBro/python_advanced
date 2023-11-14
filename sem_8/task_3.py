# Напишите функцию, которая ищет json файлы в указанной директории
# и сохраняет их содержимое в виде одноимённых pickle файлов.

# import json
import os
from pathlib import Path
import pickle


BASE_DIR = Path(__file__).resolve().parent

def convert_json_to_pickle(directory: str, filename: str):
    pickle_filename = filename.rsplit('.', 1)[0] + '.pickle'
    
    with open(os.path.join(BASE_DIR, directory, filename), 'rb') as f:
        file_data = f.read()

    with open(os.path.join(BASE_DIR,  directory, pickle_filename), 'wb') as f:
        pickle.dump(file_data, f)


def search_json_files(directory: str) -> list[str]:
    json_files = []
    for filename in os.listdir(os.path.join(BASE_DIR, directory)):
        if os.path.isfile(os.path.join(BASE_DIR,  directory, filename))\
            and filename.endswith('.json'):
            json_files.append(filename)
    
    return json_files 


def convert_all_json_files(directory: str):
    json_files = search_json_files(directory)
    for filename in json_files:
        convert_json_to_pickle(directory, filename)


convert_all_json_files('examples')