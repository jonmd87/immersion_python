"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import csv
import json
import os.path

csv_header = ["Name", "user_id", "access_leve"]


def read_file(file_path):
    data = dict()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    return data


def convert_dict_to_list(data: dict):
    lst = list()
    if data and len(data) > 0:
        for key in data.keys():
            temp_lst = [key, data[key][0], data[key][1]]
            lst.append(temp_lst)
    return lst


def write_to_file(*, file_path, header: list, body: list):
    if len(body) > 0:
        with open(file_path, "w", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(body)


src_file = "./jsons_files/users.json"
dct = read_file(src_file)
csv_body = convert_dict_to_list(dct)
dst_file = "./csv_files/users.csv"
write_to_file(file_path=dst_file, header=csv_header, body=csv_body)
