""" Реализовать функцию ​ my_func()​ , которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.

"""


def my_func(var_1, var_2, var_3):
    if var_1 > var_2:
        return (var_1 + var_3, var_1 + var_2)[var_2 > var_3]
    else:
        return (var_2 + var_3, var_1 + var_2)[var_1 > var_3]


var_list = []
while True:
    tmp_list = input('Введите два числа через пробел:\n').split(' ')
    if len(tmp_list) < 3:
        print('Вы ввели недостаточно чисел')
    elif not (tmp_list[0].isdigit() and tmp_list[1].isdigit() and tmp_list[2].isdigit()):
        print('Ошибка при вводе! Введите числа')
    else:
        var_list = int(tmp_list[0]), int(tmp_list[1]), int(tmp_list[2])
        break

result = my_func(var_list[0], var_list[1], var_list[2])
print(f'Сумма двух наибольших = {result}')
