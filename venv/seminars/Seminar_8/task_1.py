import json

"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

with open("../Seminar_7/txt_files/names&numbers", "r", encoding="utf-8") as src:
    raw_data = src.read()

dct = dict()
for item in list(raw_data.split("\n")):
    temp = item.split(" ")
    dct[temp[0].title()] = float(temp[1])


with open("./jsons_files/names&numbers.json", "w+", encoding="utf-8") as jf:
    json.dump(dct, jf, indent=2, separators=(",", ":"), ensure_ascii=False)
