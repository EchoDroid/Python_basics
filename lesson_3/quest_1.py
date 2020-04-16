""" Задание 1

Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.

"""


def my_div(var_1, var_2):
    if not var_2:
        print('Ошибка деления на ноль в функции my_div')
        return None
    if type(var_1) == str:
        var_1 = int(var_1)
    if type(var_2) == str:
        var_2 = int(var_2)
    return var_1/var_2


while True:
    tmp_list = input('Введите два числа через пробел:\n').split(' ')
    if len(tmp_list) < 2:
        print('Вы ввели недостаточно чисел')
        continue
    elif tmp_list[0].isdigit() or tmp_list[1].isdigit():
        print(f'Результат деления {tmp_list[0]} / {tmp_list[1]} = {my_div(tmp_list[0], tmp_list[1])}')
    else:
        print('Ошибка при вводе! Введите два числа')
