import random
from task_2 import ALPHABET

"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
import os


def check_suffix(suffix: str):
    if not suffix.startswith("."):
        suffix = "." + suffix

def check_directory(dir_path: str):
    dir_lst = os.listdir()
    for item in dir_lst:
        print(item)
        if os.path.isdir(item):
            while item == dir_path:
                dir_path = dir_path + random.choice(ALPHABET)
            print(dir_path)


def make_file(ext: str, dir, min_len=6, max_len=30, byte_min=256, byte_max=4096, quant=42):
    check_suffix(ext)
    check_directory(dir)

if __name__ == "__main__":
    make_file("f", "txt_files")
