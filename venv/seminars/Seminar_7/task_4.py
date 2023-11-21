import random
from task_2 import create_name

"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""


def add_point(ext: str):
    return ext if ext.startswith(".") else "." + ext


def add_suffix(file_name, suffix):
    return file_name + suffix


def make_file(ext: str, min_len=6, max_len=30, byte_min=256, byte_max=4096, quant=42):
    ext = add_point(ext)
    for i in range(quant):
        file_name = create_name(min_len, max_len)
        file_name = "./txt_files/generated_files/" + file_name
        file_name = add_suffix(file_name, ext)
        with open(file_name, "wb") as file:
            file.write(random.randbytes(random.randint(min_len, max_len)))


if __name__ == "__main__":
    make_file("txt", quant=2)
