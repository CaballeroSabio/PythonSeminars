# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list1 = []
for i in range(0, 5):
    list1.append(random.randint(0, 100))
print(list1)
def sumOfOddNums(array):
    sum = 0
    for i in range(1, len(array), 2):
        sum += array[i]
    return sum
print(sumOfOddNums(list1))