"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import csv
import json
import os.path

SIZE = 10
ZERO = "0"
HASH = "Hash"


def read_csv_file(file_path):
    with open(file_path, "r", encoding="utf-8") as src:
        src_data = list(csv.reader(src))
    return src_data


def separate_header_body(data: list):
    if data:
        header = data[0]
        body = data[1:]
        return header, body


def fill_id(data: list, index: int):
    for i in range(len(data)):
        user_id = data[i][index]
        id_len = SIZE - len(user_id)
        if id_len > 0:
            data[i][index] = str(ZERO * id_len) + user_id


def make_title(data: list, index: int):
    if data:
        for i in range(len(data)):
            data[i][index] = data[i][index].title()


def make_hash(body: list):
    for i in range(len(body)):
        name, user_id = body[i][0], body[i][1]
        body[i].append(hash(name + user_id))


def make_dict(*, keys: list, values: list):
    res_lst = list()
    for item in values:
        dct = dict.fromkeys(keys)
        for i in range(len(item)):
            dct[keys[i]] = item[i]
        res_lst.append(dct)
    return res_lst

def write_to_file(*, file_path, data: list):
    if data:
        with open(file_path, "w+", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)


def convert_data_csv_to_json(*, src_file, dst_file):
    if os.path.exists(src_file):
        src_data = read_csv_file(src_file)
        header, body = separate_header_body(src_data)
        fill_id(body, header.index("user_id"))
        make_title(body, header.index("Name"))
        header.append(HASH)
        make_hash(body)
        final_dct = make_dict(keys=header, values=body)
        write_to_file(file_path=dst_file, data=final_dct)


source = "./csv_files/users.csv"
destination = "./jsons_files/updated_users.json"
convert_data_csv_to_json(src_file=source, dst_file=destination)
