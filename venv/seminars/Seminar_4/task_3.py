"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def make_dict_from_string(data: str):
    dct = dict()
    lst = sorted(list(data.split()), reverse=True)
    for item in lst:
        dct[chr(int(item))] = item
    return dct


result = make_dict_from_string("4234 656")
print(result)