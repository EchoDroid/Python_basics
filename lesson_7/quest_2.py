""" Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто ​ и ​ костюм. У этих типов одежды существуют
параметры: ​ размер ​ (для ​ пальто) ​ и ​ рост ​ (для ​ костюма). Это могут быть обычные числа: ​
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма ​ (2*H + 0.3)​ . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""

dress_list = ('пальто', 'костюм')


class Dress:
    def __init__(self, dress_type, size, height):
        if not (dress_type.lower() in dress_list):
            self.__dress_type = None
        self.__dress_type = ''.join([dress_type[:1].upper(), dress_type[1:].lower()])
        if not 40 < size < 60:  # Российские размеры
            self.__size = 0
        self.__size = size
        if not 40 < height < 400:
            self.__height = 0
        self.__height = height
        self.__change_cloth_size()

    @property
    def cloth_size(self):
        return self.__cloth_size

    @cloth_size.setter
    def cloth_size(self, other):
        pass

    @property
    def dress_type(self):
        return self.__dress_type

    @dress_type.setter
    def dress_type(self, other: str):
        if not (other.lower() in dress_list):
            self.__dress_type = None
        self.__dress_type = ''.join([other[:1].upper(), other[1:].lower()])
        self.__change_cloth_size()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, other: int):
        if not 40 < other < 60:         # Российские размеры
            self.__size = 0
        self.__size = other
        self.__change_cloth_size()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, other: int):
        if not 40 < other < 400:
            self.__height = 0
        self.__height = other
        self.__change_cloth_size()

    def __change_cloth_size(self):
        if self.dress_type == 'Пальто':
            self.__cloth_size = self.size / 6.5 + 0.5
        elif self.dress_type == 'Костюм':
            self.__cloth_size = 2 * self.height + 0.3


class Coat(Dress):
    def __init__(self, size, height):
        super().__init__('Пальто', size, height)


class Costume(Dress):
    def __init__(self, size, height):
        super().__init__('костюм', size, height)


my_coat = Coat(52, 198)
print(my_coat.cloth_size)
my_costume = Costume(52, 198)
print(my_costume.cloth_size)
my_costume.height = 80
print(my_costume.cloth_size)
my_costume.cloth_size = 0
print(my_costume.cloth_size)
