"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""

def unicode_code(data: str):
    lst = list(set(list(data)))
    lst = list(map(lambda x: ord(x), lst))
    return sorted(lst, reverse=True)


text = ("Сформируйте список с уникальными кодами Unicode каждого "
        "символа введённой строки отсортированный по убыванию.")

result = unicode_code(text)
print(result)