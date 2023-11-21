"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
import random

MAX = 1000
MIN = -1000

def write_in_file(filename: str, number: int):
    if number > 0 and filename:
        with open(filename, "a+", encoding="utf-8") as file:
            for i in range(0, number):
                frst = random.randint(MIN, MAX)
                scnd = random.uniform(MIN, MAX)
                print(f"{frst:>5} | {scnd:.2f}", file=file)


write_in_file("./txt_files/int&float.txt", 3)