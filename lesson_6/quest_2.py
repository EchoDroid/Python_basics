""" Реализовать класс ​ Road ​ (дорога), в котором определить атрибуты: ​ length ​ (длина), ​
width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т """


class Road:
    _length = 0  # Длинна дороги, м
    _width = 0  # Ширина дороги, м
    _spec_gravity = 0  # удельная масса материлала покрытия кг/куб. м

    def __init__(self, length, width, spec_gravity):
        self._length = length
        self._width = width
        self._spec_gravity = spec_gravity

    def calc_mass(self, thickness):
        return self._width * self._length * thickness * self._spec_gravity


my_road = Road(2356, 20, 2000)
my_mass = my_road.calc_mass(0.05)
print(f'Масса материала, необходимого для дороги указанных размеров - {my_mass/1000} т')