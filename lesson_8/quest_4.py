""" Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. """

from abc import ABC, abstractmethod


# class MyValueExec(Exception):
#     __msg = ''
#
#     def __int__(self, msg):
#         MyValueExec.__msg = msg
#
#     def __str__(self):
#         return self.__msg
#
#
# class MyValidateExec(Exception):
#     def __init__(self, msg):
#         self.__msg = msg
#
#     def __str__(self):
#         return self.__msg


class Warehouse:
    def __init__(self, name):
        self.__name = name
        self.__storage = []

    def __str__(self):
        return f'Склад {self.__name} с {len(self.__storage)} товарами'


class OfficeEquipment(ABC):
    def __init__(self, s_name, s_type, f_weight, f_volume, any_info=None):
        self.__name = s_name
        self.__type = s_type
        self.__weight = f_weight
        self.__volume = f_volume
        self.__any_info = any_info

    def __str__(self):
        return f'{self.__type} "{self.__name}"'

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        if type(other) != str:
            # raise MyValueExec(str)
            pass
        self.__name = other

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, other):
        if type(other) != str:
            # raise MyValueExec(str)
            pass
        self.__type = other

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, other):
        if type(other) != float or type(other) != int:
            # raise MyValueExec(float, int)
            pass
        self.__weight = other

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, other):
        if type(other) != float or type(other) != int:
            # raise MyValueExec(float, int)
            pass
        self.__volume = other

    @property
    def any_info(self):
        return self.__any_info

    @any_info.setter
    def any_info(self, other):
        self.__any_info = other


class Printer(OfficeEquipment):
    def __eq__(self, other):
        pass


class Scanner(OfficeEquipment):
    def __init__(self, s_name, s_type, f_weight, f_volume, i_scan_speed, any_info=None):
        super().__init__(s_name, s_type, f_weight, f_volume, any_info)
        self.__scan_speed = i_scan_speed

    def __eq__(self, other):
        if type(self) != type(other):
            # raise ValueError
            return False
        elif self.name == other.name \
                and self.type == other.type \
                and self.volume == other.volume \
                and self.weight == other.weight \
                and self.scan_speed == other.scan_speed:
            return True
        else:
            return False

    @property
    def scan_speed(self):
        return self.__scan_speed

    @scan_speed.setter
    def scan_speed(self, other):
        if type(other) != int:
            # raise MyValueExec(float, int)
            pass
        elif other <= 0:
            # raise MyValidateExec(f'Для {self.type} "{self.name}" значение атрибута "scan_speed" должно быть > 0')
            pass
        else:
            self.__scan_speed = other


class Copier(OfficeEquipment):
    def __eq__(self, other):
        pass


p1 = Scanner('Xerox', 'Simple scanner', 0.5, 2, 10)
p2 = Scanner('Xerox', 'Simple scanner', 0.5, 2, 10)
p3 = Scanner('Epson', 'another scanner', 1.6, 4, 30)
print(p1)
print(type(p1))
print(type(p2))
print(f'p1 == p2: {p1 == p2}')
print(f'p2 == p3: {p2 == p3}')
print(f'p2 == 23: {p2 == 23}')
print(1)
