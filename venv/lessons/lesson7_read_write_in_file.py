# #open file for read
# file = open("../files/lorem.txt", encoding="utf-8")
# print(file)
# lst = list()
# for item in list(file):
#     if item.__contains__("\n"):
#         lst.append(str(item.removesuffix("\n")))
# file.close()
# print(*lst, sep="\n")

# #open file for append new data
# file = open("../files/lorem.txt", "a", encoding="utf=8")
# file.write("New String\n")
# file.close()

# # open bin file
# file = open("../files/bin_data", "wb", buffering=64)
# file.write(b"X" * 10)
# file.close()

# #open files with [with]
# with open("../files/lorem.txt", "r+", encoding="utf-8") as file:
#     print(list(file))
#     file.write("Work with with\n")
# file.write("This is wrong call write, error") # если раскаментировать будет ошибка

# # how to open few files with WITH
# with (
#     open("../files/bin_data", "r") as src,
#     open("../files/lorem.txt", "a", encoding="utf-8") as dst
# ):
#     dst.write(f"{str(*src)}\n")

## how to read file:
##1. file.read()
# with open("../files/lorem.txt", "r", encoding="utf-8") as file:
#     res = file.read()
#     print(res)
#     res = file.read()
#     print(res) # здесь вывод >> \n потому что read дошел до конца файла и прочел последний \n
#
# print("End")

##2. file.readline()
# with open("../files/lorem.txt", "r", encoding="utf-8") as file:
#     while res := file.readline():
#         print(res, end="")

##3. for line in file:
# with open("../files/lorem.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.replace("\n", ""))

## how to write in file
##1. write()
# with open("../files/file_for_write.txt", "a", encoding="utf-8") as file:
#     file.write("how to write in file with method write")
#     file.write("after you need to add '\\n'")

##2. writelines()
# with open("../files/file_for_write.txt", "a", encoding="utf-8") as file:
#     file.writelines("\n")
#     file.writelines("First you need to add \\n")
#     file.writelines("\n")
#     file.writelines("Write with method writelines()")

##3. print("some text", file="file_name.txt")
# with open("../files/file_for_write.txt", "a", encoding="utf-8") as file:
#     print("This string is writting with method print(), print() add \\n", file=file)

## file.tell() # where cursor in file
## file.seek(offset, whence)
## file.truncat()
