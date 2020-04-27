""" Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут ​
title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра. """

from quest_5_res import *


class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        Stationery.draw(self)
        [print(el) for el in pen_list]  # не уверен что так корректно


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        Stationery.draw(self)
        for itr in pencil_list:
            print(itr)


class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        Stationery.draw(self)
        for itr in handle_list:
            print(itr)


my_stationery = Stationery()
my_stationery.draw()
my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
my_pencil.draw()
my_handle = Handle()
my_handle.draw()
