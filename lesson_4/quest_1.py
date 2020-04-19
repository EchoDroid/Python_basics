""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами. """


from sys import argv
from excluded.my_service import try_type

script_name, total_time, payment, benefit, *_ = argv

if try_type(int, total_time, payment, benefit):
    print(int(total_time) * int(payment) + int(benefit))
else:
    print('Введите три числа через пробел')
