""" Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных."""

# Приняты дополнительные условия:
#   1. Объект класса хранит день, месяц и год
#   2. Функция извлечения даты в формате "int" записывает её в переменные класса и возвращает None
#   3. Функция провекти даты принимает три аргумента, по умолчанию 0 - то производится проверка даты класса


class Data:
    __day = 1
    __month = 1
    __year = 1

    @classmethod
    def get_int_date(cls, str_data: str):
        if cls.__validate_str(str_data):
            tmp_list = [int(el) for el in str_data.split('-')]
            cls.__day, cls.__month, cls.__year = tmp_list
        else:
            print(f'In class {cls.__name__} in functions {cls.get_int_date.__name__} data non valid!')

    @staticmethod
    def __validate_str(str_data: str):
        tmp_list = str_data.split('-')
        if len(tmp_list) != 3:
            return False
        if tmp_list[0].isdigit() or tmp_list[1].isdigit() or tmp_list[2].isdigit():
            return True
        else:
            return False

    @staticmethod
    def validate_data(day=0, month=0, year=0):
        if not day:
            day = Data.__day
        if not month:
            month = Data.__month
        if not year:
            year = Data.__year

        if not 0 < month < 13:
            return False
        is_leap = False
        # проверка на високосность
        if year % 4 == 0 and not year % 100 == 0:
            is_leap = True
        elif year % 4 == 0 and year % 400 == 0:
            is_leap = True

        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 0 < day < 32
        elif month in [4, 6, 9, 11]:
            return 0 < day < 31
        elif is_leap:
            return 0 < day < 30
        else:
            return 0 < day < 29


Data.get_int_date('10-11-1998')
print(Data.validate_data())
Data.get_int_date('29-02-2000')
print(Data.validate_data())
Data.get_int_date('29-02-400')
print(Data.validate_data())
Data.get_int_date('31-12-2020')
print(Data.validate_data())
Data.get_int_date('32-13-1200')
print(Data.validate_data(15, 6, 2019))
print(1)
