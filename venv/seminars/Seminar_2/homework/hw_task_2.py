"""
Напишите программу, которая получает целое число num и
возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

base = 16
num = 254
result = ""
for_check = num
while num > 0:
    remains = num % base
    if remains > 9:
        result = chr(97 + (remains - 10)) + result
    else:
        result = str(remains) + result
    num //= base
print(f"Шестнадцатеричное представление числа: {result.upper()}")
print(f"Проверка результата: {hex(for_check)}")
