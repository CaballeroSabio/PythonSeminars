# Реализовать алгоритм перемешивания списка.

import random

list_1 = []

for i in range(0, 21):
    list_1.append(random.randint(1, 100))

def sort(array):
    list_result1 = []
    list_result2 = []
    for i in array:
        if not i % 2:
            list_result1.append(i)
        else:
            list_result2.append(i)
    list_result1.sort()
    list_result2.sort()
    list_result1.extend(list_result2)
    return list_result1

print(f'List before sorting is {list_1}')
print(f'List after sorting is {sort(list_1)}')
