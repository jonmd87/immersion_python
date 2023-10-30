"""
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight
в качестве значения. Определите какие вещи влезут в рюкзак backpack передав его
максимальную грузоподъёмность. Результат должен быть в виде словаря {предмет:вес}
с вещами в рюкзаке и сохранен в переменную backpack.Достаточно получить один
допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
"""

items = {
    "ключи": 3.0,
    "кошелек": 4.0,
    "телефон": 2.0,
}
max_weight = 2.0
cp_max_weight = max_weight
backpack = dict()

for key, value in items.items():
    if cp_max_weight - value >= 0:
        backpack[key] = value
        cp_max_weight -= value

print(backpack)