"""
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
    среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
import random

VOWELS = "eyuioa"
ALPHABET = list(chr(i) for i in range(97, 122))


def create_name(min: int, max: int):
    result = str()
    for i in range(0, random.randint(min, max)):
        result += random.choice(ALPHABET)
    return result


def check_vowels(data: str):
    for i in data:
        if i in VOWELS:
            return data
    return str()


def write_in_file(filename: str, data: str):
    if filename and data:
        with open(filename, "a+", encoding="utf-8") as file:
            print(data, file=file)


if __name__ == "__main__":
    for i in range(random.randint(2, 8)):
        name = str()
        while len(name) < 1:
            name = check_vowels(create_name(4, 7))
        write_in_file("./txt_files/names.txt", name.capitalize())
