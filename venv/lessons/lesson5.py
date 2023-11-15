# how to make swap easy
# a = 4
# b = 2
# print(f"{a =} {b =}")
# a, b = b, a
# print(f"{a =} {b =}")

#unpack sequence
# a, b, c = input("enter three symbols: ")
# print(a, b, c)

#a, b, c = ("enter", "three", "symbols", "will be a error") # show error: -> cant unpack 4 values in 3 var

# how to fix ^
# a, b, *c = ("enter", "three", "symbols", "will be a error")
# print(a, b, c)

#how to unpack links
# link = "https://s1.skladchinmore.net/threads/zerocoder-prodvinutyj-kurs-po-mobilnym-prilozhenijam-na-flutter-flow-tarif-vip-vadim-mixalev.349717/"
# prefix, *_, suffix = link.split("/")
# print(*link.split("."), sep="\n")

# a, b, c = 1, 2, 3
# t = a, b, c
# print(a, b, c)
# print("t ", t)

# how to unpack set !!! remember set has hash!!
# data = {100, 12, 3, 40, 5, 6, 7}
# a, b, c, *d, e = data
# print(a, b, c, d, e, data)

#iter(object, [, sentinel])
# data = {100, 12, 3, 40, 5, 6, 7}
# list_iter = iter(data)
# print(list_iter)
# print(type(list_iter))
# print(*list_iter)
# print(*list_iter, sep="\n")

#generator
# a = (chr(i) for i in range(97, 123) )
# print(a)
# print(*a, sep="\n")

# gener = (i for i in range(0, 1000) if i % 2 == 0)
# print(type(gener), gener.__sizeof__())
# print(*gener, sep="\t")
#
# lst = [i for i in range(0, 1000) if i % 2 == 0]
# print(type(lst), lst.__sizeof__())
# print(*lst, sep="\t")
#
# st = {i for i in range(0, 10) if i % 2 == 0}
# print(type(st))
# print(*st)
#
# dct = {chr(i): i for i in range(97, 100)}
# print(type(dct))
# print(dct)

