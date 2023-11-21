import json
import os.path

"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""


def get_user_data():
    data = dict()
    user_name = input("Enter your name: ")
    user_id = int(input("Enter your id: "))
    user_access_level = int(input("Enter your acces level: "))
    data[user_name] = [user_id, user_access_level]
    return data


def read_data(file_path):
    data = dict()
    if os.path.exists(file_path) and os.stat(file_path).st_size != 0:
        with open(file_path, "r", encoding="utf") as jf:
            data = dict(json.load(jf))
            print(type(data))
            print(data)
    return data


def write_to_file(data: dict, file_path: str):
    with open(file_path, "w+", encoding="utf-8") as js:
        json.dump(data, js, separators=(",", ":"), ensure_ascii=False, indent=2)


file_path = "./jsons_files/users.json"

while True:
    users = read_data(file_path)
    users.update(get_user_data())
    write_to_file(users, file_path)
    answer = input("Do you want to proceed? y/n: ")
    if answer == "n":
        break
