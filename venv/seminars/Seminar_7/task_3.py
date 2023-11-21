from task_2 import write_in_file

"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало
"""


def get_data_from_file(filename):
    lst = list()
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                lst.append(line)
    return lst


def remove_end_of_string(data: list):
    for i in range(len(data)):
        data[i] = data[i].strip()
    return data


def multiply_numbers(data: list):
    for i in range(len(data)):
        temp = data[i].split("|")
        data[i] = int(temp[0]) * float(temp[1])
    return data


def change_data(number: float, name: str):
    if number > 0:
        return str(name.lower()) + " " + str(round(number))
    else:
        return (name.upper()) + " " + str(abs(number))


def join_lists(numbers: list, names: list):
    result = list()
    if numbers and names:
        size = max([len(numbers), len(names)])
        for i in range(size):
            result.append(change_data(numbers[i % len(numbers)], names[i % len(names)]))
    return result


raw_data = get_data_from_file("./txt_files/int&float.txt")
numbers_list = multiply_numbers(remove_end_of_string(raw_data))

raw_data = get_data_from_file("./txt_files/names.txt")
names_list = remove_end_of_string(raw_data)

final_lst = join_lists(numbers_list, names_list)
for item in final_lst:
    write_in_file("./txt_files/names&numbers", item)
