# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = input('Введите число: ')

def day_of_week(a):
    if a == 1:
        print('Понедельник')
    elif a == 2:
        print('Вторник')
    elif a == 3:
        print('Среда')
    elif a == 4:
        print('Четверг')
    elif a == 5:
        print('Пятница')
    elif a == 6:
        print('Суббота')
    elif a == 3:
        print('Воскресенье')
    return a

if a.isdigit():
    day_of_week(int(a))
else:
    print('Введено неверное значение')

