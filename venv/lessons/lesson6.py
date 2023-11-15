import random
from sys import path as p
from sys import argv
# using random
# for i in range(1, 10):
#     print(random.randint(1, 10000))

# print(*p)
print("start")
for i in range(1, len(argv)):
    print(argv[i])
print("stop")