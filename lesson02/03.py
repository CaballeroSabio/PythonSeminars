# Задать список из n чисел последовательности (1+ 1\n)^n и вывести на экран сумму.

list_res = []
num = int(input('Enter a integer: '))
for n in range(1, num + 1):
    x = round((1 + 1 / n) ** n, 2)
    list_res.append(x)
print(list_res)
sum_res = sum(list_res)
print(sum_res)