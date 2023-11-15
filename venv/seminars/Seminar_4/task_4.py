from random import randint
"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""


def sort_(data: list):
    ind = 0
    while ind < len(data):
        for first in range(len(data) - 1):
            if data[first] > data[first + 1]:
                data[first + 1], data[first] = data[first], data[first + 1]
        ind += 1
    return data

lst = [randint(-1000, 1000) for _ in range(10)]
print(lst)
result = sort_(lst)
print(result)