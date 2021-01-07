""" Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой. """


class DivByZeroException(Exception):
    def __init__(self, notice):
        self.__notice = notice

    def __str__(self):
        return self.__notice


a = 5
b = 0
try:
    if not b:
        raise DivByZeroException('Ошибка деления на ноль! Это пользовательское исключение')
    else:
        c = a / b
        print(c)
except DivByZeroException as err:
    print(err)
except ZeroDivisionError:
    print('Сработало стандартное исключение python деления на ноль')


# Проверка гипотезы - как встроить пользовательское исключение в стандартные методы классов
# class int(int):
#     def __truediv__(self, other):
#         if not other:
#             raise DivByZeroException('Ошибка деления на ноль! Это пользовательское исключение')
#         else:
#             return int.__truediv__(self, other)
#
#
# a = int(5)
# b = int(0)
# try:
#     c = a / b
# except DivByZeroException as err:
#     print(err)
