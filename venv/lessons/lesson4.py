def my_func(a, /, b, c, *, d):
    print(a, b, c, d)


my_func(1, 2, c=3, d=4)


# map function + lambda
text = ["Hi", "heLLO", "CHAO"]
res = map(lambda x: x.lower(), text)
print(res)
print(*res)

# filter func
numbers = [10, 33, 2, 34, 65, 36, 22, -23, 0]
res = filter(lambda x: x < 10, numbers)
print(res)
print(*res)

# zip func
names = ["Ivan", "Sasha", "Daria"]
salaries = [200, 220, 330]
ages = [1994, 1995, 1996]

for name, age, salary in zip(names, ages, salaries):
    print(f"{name= } {age =} {salary =}")
