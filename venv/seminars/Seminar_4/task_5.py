"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""


# rstrip - Возвращает копию указанной строки,
# с конца которой устранены указанные символы

def calc_reward(lst_names: str, lst_salary: int, lst_reward: str):
    dct = dict()
    if len(lst_names) == len(lst_salary) and len(lst_names) == len(lst_reward):
        for i in range(len(lst_names)):
            dct[lst_names[i]] = lst_salary[i] * float(lst_reward[i].rstrip("%")) / 100
            print(dct)
    return dct

names = ['Борис', 'Иван', 'Петр', "Сергей"]
salaries = [10000, 12000, 16000, 14000]
awards = ['12.35%', '10.25%', '7.75%', '8.85%']

print(calc_reward(names, salaries, awards))
