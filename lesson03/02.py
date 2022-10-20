# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

list1 = []
for i in range(0, 5):
    list1.append(random.randint(0, 10))
print(list1)
list2 = []

def prod_of_pairs_of_nums (array):
    for i in range(0, len(array) // 2):
        a = array[i] * array [-i - 1]
        list2.append(a)
    if len(array) % 2:
        b = array[(len(array) // 2)] ** 2
        list2.append(b)
    return list2

print(prod_of_pairs_of_nums(list1))