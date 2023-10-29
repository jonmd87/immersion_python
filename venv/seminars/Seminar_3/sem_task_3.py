"""
Задание №3
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

cort = (1, 2, 3, 4, 'turtle', 'dog', 'donkey', ['l', 'i', 's', 't'], True, False)
my_dict = dict()

for item in cort:
    temp = type(item)
    lst = list()
    for i in cort:
        if type(i) == temp:
            lst.append(i)

    my_dict[temp] = lst
print(my_dict)


