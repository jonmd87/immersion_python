"""
Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
Используйте правило для проверки:
“Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


negative_border = 1
positive_border = 100_000
simple_numbers = (2, 3, 5, 7)
flag = False


user_answer = int(input("Enter positive number less than 100.000 and more than 0: "))
if user_answer <= negative_border or user_answer > positive_border:
    print("Число должно быть больше 1 и меньше 100000")
else:
    if user_answer in simple_numbers:
        flag = False
    else:
        for item in simple_numbers:
            if user_answer % item == 0:
                flag = True

print(f"{user_answer} является составным числом" if flag == True else f"{user_answer} является простым числом")
