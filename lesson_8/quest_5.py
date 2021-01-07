""" Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь. """

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

    def take_in_warehouse(self, subject, count: int):
        if not issubclass(type(subject), OfficeEquipment):
            # raise MyValueExec()
            pass
        else:
            result = self.find_in_warehouse(subject, count)
            if not result + 1:
                self.__storage.append([subject, count])
            else:
                self.__storage[result][1] += count

    def find_in_warehouse(self, subject, count=0):
        if not issubclass(type(subject), OfficeEquipment):
            # raise MyValueExec()
            return None

        result = -1
        for i, itr in enumerate(self.__storage):
            if itr[0] == subject:
                result = i
                return result
        return result

    def send_to_unit(self, unit, subject, count=0):
        if not issubclass(type(subject), OfficeEquipment):
            # raise MyValueExec()
            pass

        result = self.find_in_warehouse(subject, count)
        if not result + 1:
            # raise MyNotFind()
            pass
        else:
            if not count:
                self.__storage.pop(result)
            elif self.__storage[result][1] < count:
                print(f'На складе {self.__name} имеется {self.__storage[result][1]} товаров, '
                      f'запрошена передача {count} товаров')
                self.__storage.pop(result)
            else:
                self.__storage[result][1] -= count


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
        if type(self) != type(other):
            # raise MyValueExec("<class Scanner>")
            return False
        elif self.name == other.name \
                and self.type == other.type \
                and self.volume == other.volume \
                and self.weight == other.weight:
            return True
        else:
            return False


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
        if type(self) != type(other):
            # raise MyValueExec("<class Scanner>")
            return False
        elif self.name == other.name \
                and self.type == other.type \
                and self.volume == other.volume \
                and self.weight == other.weight:
            return True
        else:
            return False


sk = Warehouse('Мой текущий склад')
p1 = Scanner('Xerox', 'Simple scanner', 0.5, 2, 10)
p2 = Printer('Xerox', 'Simple printer', 0.8, 2, 10)
p3 = Scanner('Epson', 'another scanner', 1.6, 4, 30)
sk.take_in_warehouse(p1, 10)
sk.take_in_warehouse(p2, 3)
sk.take_in_warehouse(p3, 1)
sk.take_in_warehouse(p3, 10)
sk.take_in_warehouse(p1, 11)
tmp = sk.find_in_warehouse(p2)
sk.send_to_unit('Другой склад', p1, 5)
print(1)