""" Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата. """


class ComplexNum:
    def __init__(self, x=0, iy=0):
        self.__x = x
        self.__iy = iy

    def __str__(self):
        return f'{self.x}{"+" if self.iy > 0 else "-"}i{abs(self.iy)}'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, other):
        self.__x = other

    @property
    def iy(self):
        return self.__iy

    @iy.setter
    def iy(self, other):
        self.__iy = other

    def __add__(self, other):
        if type(other) == ComplexNum:
            return ComplexNum(self.x + other.x, self.iy + other.iy)
        elif type(other) in [int, float]:
            return ComplexNum(self.x + other, self.iy)
        else:
            raise ValueError(f'Ошибка сложения {type(self)} и {type(other)} - '
                             f'операнд должен быть {type(self)} или {type(1)} или {type(1.1)}')

    def __sub__(self, other):
        if type(other) == ComplexNum:
            return ComplexNum(self.x - other.x, self.iy - other.iy)
        elif type(other) in [int, float]:
            return ComplexNum(self.x - other, self.iy)
        else:
            raise ValueError(f'Ошибка сложения {type(self)} и {type(other)} - '
                             f'операнд должен быть {type(self)} или {type(1)} или {type(1.1)}')

    def __mul__(self, other):
        if type(other) == ComplexNum:
            return ComplexNum(self.x * other.x - self.iy * other.iy, self.x * other.iy + other.x * self.iy)
        elif type(other) in [int, float]:
            return ComplexNum(self.x * other, self.iy * other)
        else:
            raise ValueError(f'Ошибка сложения {type(self)} и {type(other)} - '
                             f'операнд должен быть {type(self)} или {type(1)} или {type(1.1)}')

    def __truediv__(self, other):
        if type(other) == ComplexNum:
            return ComplexNum((self.x * other.x - self.iy * other.iy) / (other.x*other.x + other.iy*other.iy),
                              (self.iy*other.x - self.x*other.iy) / (other.x*other.x + other.iy*other.iy)
                              )
        elif type(other) in [int, float]:
            return ComplexNum(self.x / other, self.iy / other)
        else:
            raise ValueError(f'Ошибка сложения {type(self)} и {type(other)} - '
                             f'операнд должен быть {type(self)} или {type(1)} или {type(1.1)}')


my_cmp1 = ComplexNum(1, 2)
my_cmp2 = ComplexNum(5, 8)
print(my_cmp1 + my_cmp2)
print(my_cmp1 - my_cmp2)
print(my_cmp1 * my_cmp2)
print(my_cmp1 / my_cmp2)
print(my_cmp1 + 10)
print(my_cmp1 - 10)
print(my_cmp1 * 10)
print(my_cmp1 / 10)
print(my_cmp1 + 11.11)
print(my_cmp1 + '10')
