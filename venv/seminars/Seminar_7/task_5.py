import random

import task_4

"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

FILE_EXTENSIONS = ["txt", "doc", "docs", "pdf"]


def create_files_either(files=1, *args):
    if len(*args) > 0:
        for i in range(files):
            ext = random.choice(*args)
            task_4.make_file(ext, quant = 1)


if __name__ == "__main__":
    create_files_either(2, FILE_EXTENSIONS)
