"""
Задание №2
Погружение в Python | Коллекции
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

data = [1, -2, 3.14, 'heLlo', 'WORLD']

for item in data:
    try:
        print(int(item))
        print(float(item))
        if type(item) == str and item.islower():
            print(item.islower())
    except ValueError:
        print(f"Can't convert in int or in float {item}")
