""" Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. """

from abc import ABC, abstractmethod, abstractproperty

class MyNameExec(Exception):
    def __str__(self):
        return 'Ошибка при вводе данных! Имя должно быть типа str!'

class Warehouse:
    def __init__(self, name):
        self.__name = name
        self.__storage = []

    def __str__(self):
        return f'Склад {self.__name} с {len(self.__storage)} товарами'


class OfficeEquipment(ABC):
    def __init__(self, s_name, s_type, f_weight, f_volume, any_info=None) -> None:
        pass

    def __str__(self) -> str:
        pass

    @abstractmethod
    @property
    def name(self) -> str:
        pass

    @abstractmethod
    @name.setter
    def name(self, other) -> None:
        pass

    @abstractmethod
    @property
    def type(self) -> str:
        pass

    @abstractmethod
    @type.setter
    def type(self, other) -> None:
        pass

    @abstractmethod
    @property
    def weight(self) -> float:
        pass

    @abstractmethod
    @weight.setter
    def weight(self, other) -> None:
        pass

    @abstractmethod
    @property
    def volume(self) -> float:
        pass

    @abstractmethod
    @volume.setter
    def volume(self, other) -> None:
        pass

    @abstractmethod
    @property
    def any_info(self) -> dict:
        pass

    @abstractmethod
    @any_info.setter
    def any_info(self, other) -> None:
        pass


class Printer(OfficeEquipment):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other):
        if type(other) != str:
            raise MyNameExec
        self.__name = other

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, other):
        if type(other) != str:
            raise MyNameExec
        self.__type = other

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, other):
        if type(other) != float or type(other) != int:
            raise MyNameExec
        self.__weight = other

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, other):
        if type(other) != float or type(other) != int:
            raise MyNameExec
        self.__volume = other

    @property
    def any_info(self):
        return self.__any_info

    @any_info.setter
    def any_info(self, other):
        self.__any_info = other

a = Printer('n', 't', 1, 1)
print(1)