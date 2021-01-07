""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами. """


from sys import argv
from excluded.my_service import try_type

script_name, total_time, payment, benefit, *_ = argv

if try_type(float, total_time, payment, benefit):
    print(round(float(total_time) * float(payment) + float(benefit), 2))
else:
    print('Введите три числа через пробел')
