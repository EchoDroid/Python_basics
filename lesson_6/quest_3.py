""" Реализовать базовый класс ​ Worker ​ (работник), в котором определить атрибуты: ​
name, surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров). """


class Worker:
    _name = ''
    _surname = ''
    _position = ''
    _income = {}


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, salary: float, bonus: float):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {'salary': salary, 'bonus': bonus}

    def get_full_name(self):
        return self._name + ' ' + self._surname

    def get_total_income(self):
        return self._income.get('salary') + self._income.get('bonus')


my_pos_1 = Position('Иван', 'Иванов', 'Менеджер', 9600.0, 4000.0)
my_pos_2 = Position('Пётр', 'Синицин', 'Старший менеджер', 12300.0, 6000.0)

print(my_pos_1.get_full_name())
print(my_pos_1)
print(my_pos_1.get_total_income())
print(my_pos_2.get_full_name())
print(my_pos_2)
print(my_pos_2.get_total_income())
