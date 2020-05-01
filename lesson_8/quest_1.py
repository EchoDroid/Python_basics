""" Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных."""


class Data:
    def __init__(self, data: str):
        self.str_data = data
        if Data.validate_str(data):
            self.day, self.month, self.year = Data.get_int_date(data)
        else:
            self.day = self.month = self.year = 0

    @staticmethod
    def get_int_date(str_data: str):
        tmp_list = str_data.split('-')
        return int(tmp_list[0]), int(tmp_list[1]), int(tmp_list[2])

    @staticmethod
    def validate_str(str_data: str):
        tmp_list = str_data.split('-')
        if len(tmp_list) != 3:
            return False
        if tmp_list[0].isdigit() or tmp_list[1].isdigit() or tmp_list[2].isdigit():
            return True
        else:
            return False

    @staticmethod
    def validate_data(day: int, month: int, year: int):
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


md1 = Data('10-11-1998')
md2 = Data('10-111998')
print(Data.validate_data(31, 11, 1998))
print(Data.validate_data(30, 11, 1998))
print(Data.validate_data(30, 2, 2000))
print(Data.validate_data(29, 2, 2000))
print(Data.validate_data(29, 2, 1999))
print(Data.validate_data(29, 2, 400))
print(Data.validate_data(29, 2, 401))
print()