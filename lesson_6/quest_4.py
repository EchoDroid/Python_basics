""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: ​
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
(TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат. """


class Car:
    _type = 'Машина'
    _is_police = False

    def __init__(self, name: str, speed: float, color: str):
        self._name = name
        self._speed = speed
        self._color = color

    def go(self):
        print(f'{self._type} "{self._name}" поехала')

    def stop(self):
        print(f'{self._type} "{self._name}" остановилась')

    def turn(self, direction):
        print(f'{self._type} "{self._name}" повернула на {direction}')

    def show_speed(self):
        print(f'{self._type} "{self._name}" имеет текущую скорость {self._speed}')

    def set_as_police(self):
        self._is_police = True


class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self._type = 'Городской автомобиль'
        self._name = name
        self._speed = speed
        self._max_speed = 60
        self._color = color

    def show_speed(self):
        if self._speed >= self._max_speed:
            print(f'{self._type} "{self._name}" превысил допустимую скорость ({self._max_speed}) - {self._speed}')
        else:
            Car.show_speed(self)


class WorkCar(TownCar):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self._type = 'Грузовой автомобиль'
        self._name = name
        self._speed = speed
        self._color = color
        self._max_speed = 40


class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self._type = 'Спортивный автомобиль'
        self._name = name
        self._speed = speed * 2
        self._color = color


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self._type = 'Полицейский автомобиль'
        self._name = name
        self._speed = speed
        self._color = color
        self._is_police = True


car_1 = TownCar('первая', 30, 'красный')
car_1.go()
car_1.show_speed()
car_2 = TownCar('вторая', 80, 'жёлтый')
car_2.go()
car_2.show_speed()
car_3 = WorkCar('третья', 20, 'зелёный')
car_3.go()
print(car_3._name)
print(car_3._is_police)
car_3.show_speed()
car_4 = WorkCar('четвёртый', 50, 'синий')
car_4.show_speed()
car_5 = SportCar('пятый', 50, 'фиолетовый')
car_5.show_speed()
car_6 = PoliceCar('шестая', 50, 'пурпурный')
car_6.go()
print(car_6._is_police)
