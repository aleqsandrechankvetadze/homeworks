import random

my_list = []

for i in range(15):
    my_list.append(random.randint(1, 100))
print(my_list)

for i in my_list:
        if i % 3 == 0:
            print(i)


