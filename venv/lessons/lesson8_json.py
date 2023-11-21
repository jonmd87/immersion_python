import json

##  serialization deseerialization
# JSON (JavaScript Obkect Notation)

# load from json file (how to convert JSON obkect in Python obkects)
#
# json_file = json.load("jsonFile") # return load json file to dict or list
# json_text = json.loads("json_text") # return load json string to dict or list
# with open("./json_files/simple_template.json", "r", encoding="utf-8") as jf:
#     json_file = json.load(jf)
# print(type(json_file))
# for k, v in json_file.items():
#     print(f"{k=}: {v=}")
#     if isinstance(v, dict) and k == "address":
#         for key, val in v.items():
#             print(f"\t{key=} {val=}")

## json string
# json_str = """
# {
#     "user":"vanI",
#     "name":"Ivan",
#     "id":1234
# }
# """
# print(type(json_str))
# json_dct = json.loads(json_str)
# print(type(json_dct))
# for k, v in json_dct.items():
#      print(f"{k=}({type(k)=}): {v=}({type(v)=})")

## json.dump() (how to convert PYthon objects to JSON objects)
# py_dct = {
#     "user":"vanI",
#     "name":"иван",
#     "id":1234,
#     "hobbies":["reading", "programing"],
#     "children": [
#         {
#             "first_name": "alice",
#             "age":5
#         },
#         {
#             "first_name": "anton",
#             "age":7
#         }
#     ]
# }
# print(type(py_dct))
# print(py_dct)
# with open("./json_files/dict_to_json.json", "w", encoding="utf-8") as jf:
#     json.dump(py_dct, jf, ensure_ascii=False)

## how to save python object in json file as string json.dumps()
# py_dct = {
#     "user":"vanI",
#     "name":"иван",
#     "id":1234,
#     "hobbies":["reading", "programing"],
#     "children": [
#         {
#             "first_name": "alice",
#             "age":5
#         },
#         {
#             "first_name": "anton",
#             "age":7
#         }
#     ]
# }
# print(type(py_dct))
# print(py_dct)
#
# dict_to_json_text = json.dumps(py_dct, ensure_ascii=False)
# with open("./json_files/dict_to_json.json", "w", encoding="utf-8") as jf:
#     json.dump(py_dct, jf, ensure_ascii=False)
# print(type(dict_to_json_text))
# print(dict_to_json_text)
# txt = "Hello, World!"
# dct = {key: value for key, value in enumerate(txt)}
# for k, v in dct.items():
#     print(f"{k=}: {v=}")

