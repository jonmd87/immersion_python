# def my_func(a, /, b, c, *, d):
#     print(a, b, c, d)
#
# my_func(1, 2, c=3, d=4)


# # map function + lambda
# text = ["Hi", "heLLO", "CHAO"]
# res = map(lambda x: x.lower(), text)
# print(res)
# print(*res)

# # filter func
# numbers = [10, 33, 2, 34, 65, 36, 22, -23, 0]
# res = filter(lambda x: x < 10, numbers)
# print(res)
# print(*res)
#
# # zip func
# names = ["Ivan", "Sasha", "Daria"]
# salaries = [200, 220, 330]
# ages = [1994, 1995, 1996]
#
# for name, age, salary in zip(names, ages, salaries):
#     print(f"{name= } {age =} {salary =}")


# #max & min подставь вместо max min
# lst1 = []
# lst2 = [42, -40, 84]
# lst3 = [("Ivan", 42), ("Jana", 43)]
# print(max(lst1, default=None))
# print(max(*lst2))
# print(max(lst3, key=lambda x: x[1]))
# print(sorted(lst3, key=lambda x: x[0]))
# print(sorted(lst3, key=lambda x: x[0], reverse=True))

# #sum
# lst_1 = [12, 22, 34, 55, 66]
# print(sum(lst_1)) # >>> 189
# print(sum(lst_1, start=11)) # >>> 200 (return all sum + 11)

# #all
# lst_1 = [12, 22, 34, 55, 66]
# if all(map(lambda x: x > 20, lst_1)):
#     print("All numbers are more then 20")
# else:
#     print("Some numbers are less than 20")

# #chr(int)
# print(chr(97)) # >>> a
# print(chr(1105)) # >>> ё
# print(chr(128519)) # >>> 😇

# #chr(int)
# print(ord('a')) # >>> 97
# print(ord('ё')) # >>>  1105
# print(ord('😇')) # >>> 😇 128519

#locals()

SIZE = 10

def func(a, b, c):
    x = a + b
    print(locals()) # >>> {'a': 1, 'b': 2, 'c': 3, 'x': 3}
    z = (x + c)
    return z

func(1, 2, 3)