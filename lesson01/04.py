# 3. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = input('Введите номер четверти: ')

def number_of_a_quarter(n):
    if n < 1 or n > 4:
        print('Введено неверное значение')
    elif n == 1:
        print('x > 0 and y > 0')
    elif n == 2:
        print('x < 0 and y > 0')
    elif n == 3:
        print('x < 0 and y < 0')
    elif n == 4:
        print('x > 0 and y < 0')
    return n

if n.isdigit():
    number_of_a_quarter(int(n))
else:
    print('Введено неверное значение')
