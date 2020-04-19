""" Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию ​ count() и cycle() модуля ​ itertools​ . Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено. """


from itertools import (count,
                       cycle,
                       )


def my_useless_count(int_start: int, int_stop: int):
    for itr in count(int_start):
        print(itr, end='')

        if itr == int_stop:
            break
    print()


def my_useless_cycle(template_list, itr_count: int):
    counter = 0
    for itr in cycle(template_list):
        print(itr, end='')

        if counter >= itr_count:
            break
        counter += 1
    print()


my_useless_count(3, 10)
my_useless_cycle('ABC', 6)
