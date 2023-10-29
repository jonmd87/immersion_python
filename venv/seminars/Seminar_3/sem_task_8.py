"""
Задание №8

✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
    ✔ Какие вещи взяли все три друга
    ✔ Какие вещи уникальны, есть только у одного друга
    ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""

def print_result(message, data):
    print("\n", message, data)

# ✔ Какие вещи взяли все три друга
# intersection - возвращает пересечение — элементы данного множества,
# также присутствующие в указанных объектах.

data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
        "Витя": ("Палатка", "Котелок", "Топор"),
        "Петя": ("Палатка", "Котелок", "Топор", "Спирт"),
        "Саша": ("Палатка", "Спирт")}

#Какие вещи взяли все три друга
lst = list()
for key, value in data.items():
    for item in value:
        lst.append(item)
lst = list(set(lst))
print_result("All friends got these things: ", lst)

#Какие вещи уникальны, есть только у одного друга
# teacher solution:
# st = set()
# for s in data:
#     st = set(data[s])
#     for f in data:
#         if s != f:
#             st = st.difference(set(data[f]))
#     if st:
#         print(f"Только {s} имеет {st}")
#

#my solution it works but don't show name of person
lst.clear()
for value in data.values():
    for item in value:
        lst.append(item)
temp_dct = dict.fromkeys(set(lst), 0)
while len(lst) != 0:
    temp_dct[lst.pop(0)] += 1
lst.clear()
for key, val in temp_dct.items():
    if val == 1:
        lst.append(key)

print_result("Unique things: ", lst)

# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

