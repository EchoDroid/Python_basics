""" Программа принимает действительное положительное число ​ x и целое отрицательное число
y. Необходимо выполнить возведение числа ​ x в степень ​ y ​ . Задание необходимо реализовать
в виде функции ​ my_func(x, y)​ . При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

"""


def try_type(var, var_type):
    try:
        var_type(var)
        return True
    except ValueError:
        return False


def my_func_pow(x, y):
    res_2 = x
    for i in range(abs(y) - 1):
        res_2 *= x
    return x**y, res_2 if y > 0 else 1/res_2


while True:
    tmp_list = input('Введите два числа через пробел:\n').split(' ')
    if len(tmp_list) < 2:
        print('Вы ввели недостаточно чисел')
    elif not (try_type(tmp_list[0], int) and try_type(tmp_list[1], int)):
        print('Ошибка при вводе! Введите числа')
    else:
        print(f'Результат: {my_func_pow(int(tmp_list[0]), int(tmp_list[1]))}')
        break
