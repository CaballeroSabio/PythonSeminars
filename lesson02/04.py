# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

def new_list(num, p1, p2, p3):
    res_list = []
    positions = [p1, p2, p3]
    result = 1
    for i in range(-num, num + 1):
        res_list.append(i)
    maxindex = len(res_list) - 1
    minindex = len(res_list)
    for n in positions:
        if n > maxindex or n < -minindex:
            return print('Invalid index value specified')
        result *= res_list[n]
    return print(f'In the list {res_list} the product of values with indices {p1}, {p2}, {p3} is {result}')

number = int(input('Enter an integer: '))

poz1 = int(input('Enter first number index: '))
poz2 = int(input('Enter second number index: '))
poz3 = int(input('Enter third number index: '))

new_list(number, poz1, poz2, poz3)

exit()
# declare a list and fill it with numbers in the range from -20 to 21
list = [x for x in range(-20, 21)]
print(list)
# create a list of items
positions = [1, 3, 6]
res = list[1] * list[3] * list[6]
print(res)
