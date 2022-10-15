# Задание 1. Подсчитать сумму цифр в вещественном числе.

print('first working solution')
#объявляем переменную и записываем в неё введённое пользователем число
num = input("Введите число: ")
sum = 0
for i in num:
    if (i.isdigit()):
        sum += int(i)
print(sum)

exit()

# def sum(n):
#     count = 0
#     while count <= len(n):
#         for i in n:
#             res = i + i
#             count += 1
#     print(res)
#     # return res
# sum(n)
# if n.isdigit():
#     sum(n)
# else:
#     print('Введено неверное значение')

# создаём рекурсивную функцию для подсчёта сумма цифр числа
n = 2.55
def isfloat(n):
    if isinstance(n, int):
        return n
    if isinstance(n, float):
        n *= 10
        if n % 1 == 0:
            n = int(n)
        return isfloat(n)
    else:
        return n
# if n.isdigit():
print(isfloat(n))


