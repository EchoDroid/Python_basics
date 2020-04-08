"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.
"""


def print_tnv(my_var):
    print(f'{type(my_var)} и значение {my_var}')


def print_sep(sep, count):
    print(sep * count)


def try_type(var, var_type):
    try:
        var_type(var)
        return True
    except ValueError:
        return False


my_str = 'test string'
my_int = 100
my_float = 100.50
my_list = ['list-1', 'list-2', 'list-3']
my_dict = {'1': 'dict-1', '2': 'dict-2', '3': 'dict-3'}

print_tnv(my_str)
print_sep('-', 100)
print_tnv(my_int)
print_sep('-', 100)
print_tnv(my_float)
print_sep('-', 100)
print_tnv(my_list)
print_sep('-', 100)
print_tnv(my_dict)
print_sep('-', 100)

my_str = input('Введите любую текстовую строку: ')
print('Вы ввели')
print_tnv(my_str)
print_sep('-', 100)

user_str = input('Введите любое целое число: ')
if try_type(user_str, int):
    my_int = int(user_str)
    print('Вы ввели')
    print_tnv(my_int)
    print_sep('-', 100)
else:
    print('Вы ошиблись при вводе')
    print_sep('-', 100)

user_str = input('Введите любое дробное число: ')
if try_type(user_str, float):
    my_int = float(user_str)
    print('Вы ввели')
    print_tnv(my_int)
    print_sep('-', 100)
else:
    print('Вы ошиблись при вводе')
    print_sep('-', 100)

my_list = []
while len(my_list) < 3:
    user_str = input(f'Введите любое любое значение №{len(my_list)+1}: ')
    if try_type(user_str, int):
        my_list.append(int(user_str))
    elif try_type(user_str, float):
        my_list.append(float(user_str))
    else:
        my_list.append(user_str)
else:
    print_tnv(my_list)
    print_sep('-', 100)
