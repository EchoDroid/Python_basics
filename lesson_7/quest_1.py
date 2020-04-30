""" Реализовать класс ​ Matrix ​ (матрица). Обеспечить перегрузку конструктора класса (метод __init__()​ ),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода ​ __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода ​ __add__() для реализации операции сложения двух
объектов класса ​ Matrix ​ (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д. """


def yld_itr_list(mat_list: list):
    for itr in mat_list:
        yield itr


class Matrix:
    def __init__(self, matrix_list: list):
        self.__data = [matrix_list[0]]
        for itr in matrix_list[1:]:
            if len(itr) != len(self.__data[0]):     # если не все строки одинаковы по длинне
                print('Ошибка при создании экземпляра класса Matrix - переданный лист не матрица')
                self.__data = None
                break
            self.__data.append(itr)

    @property
    def data(self):
        return self.__data

    def __str__(self):
        return '\n'.join(' '.join(map(str, itr)) for itr in self.data)

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):    # Если матрицы разные
            return None
        itr = yld_itr_list(self.data)
        jtr = yld_itr_list(other.data)
        return Matrix([list(map(lambda x, y: x + y, next(itr), next(jtr))) for _ in range(len(self.data))])


mat_1 = Matrix([[1, 1, 1, 1, 6],
                [2, 2, 2, 1, 2],
                [3, 3, 3, 1, 3]])
mat_2 = Matrix([[3, 3, 3, 2, 9],
                [2, 2, 2, 2, 7],
                [1, 1, 1, 2, 5]])
mat_3 = mat_1 + mat_2
print(mat_3)
