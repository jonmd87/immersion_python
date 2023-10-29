name = "john"
age = 35

print("my name is {} and i am {} years old".format(name, age))
print(f"my name is {name} and i am {age} years old")

my_list = [10, 20, 30, 40, 20,  50, 60]

for item in my_list:
    print(f"{item:>10}") # выравнивает по краю
    print(f"{item:<20}")

print(f"{my_list = }") # выведит my_list на экран
print(my_list.index(20,2)) # найдет индекс второго значение 20
