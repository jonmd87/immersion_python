
"""
Задание №7
Погружение в Python | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
        "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ")

lst = list(text)
dct = dict.fromkeys(set(lst), 0)
while len(lst) != 0:
    dct[lst.pop(0)] += 1

# checking results
print("len", len(text))
print(sum(dct.values()))