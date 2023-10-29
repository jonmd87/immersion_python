import fractions

"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.
"""
frac1 = "3/4"
frac2 = "4/5"


temp_str = fract1.split("/")
fract1_a = int(temp_str[0])
fract1_b = int(temp_str[1])
temp_str = fract2.split("/")
fract2_a = int(temp_str[0])
fract2_b = int(temp_str[1])

numerate = fract1_a * fract2_b + fract1_b * fract2_a
denumerate = fract1_b * fract2_b

print(f"Сумма дробей: {numerate}/{denumerate}")
print(f"Произведение дробей: {fract1_a * fract2_a}/{fract1_b * fract2_b}")
f_1 = fractions.Fraction(fract1)
f_2 = fractions.Fraction(fract2)
print(f"Сумма дробей: {f_1 + f_2}")
print(f"Произведение дробей: {f_1 * f_2}")
