"""
Задание №6
Погружение в Python | Коллекции
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

data = "bb zzzzz dddd ccc a".split()
shift = len(max(data))

for index, element in enumerate(sorted(data)):
    print(f"{index}. {element:>{shift}}")

