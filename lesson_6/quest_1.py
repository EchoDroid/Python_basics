""" Создать класс ​ TrafficLight ​ (светофор) и определить у него один атрибут ​ color ​ (цвет) и метод
running ​ (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) ​ — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""


from time import sleep


class TrafficLight:
    __color = ''
    _on = False

    def __init__(self):
        print('Экземпляр класса TrafficLight успешно создан')

    def turn_color(self, color: str):
        self.__color = color
        print(self.__color)

    def on_traffic_light(self):
        self._on = True
        # while self._on:
        self.__color = 'красный'
        print(self.__color)
        sleep(7)
        self.__color = 'жёлтый'
        print(self.__color)
        sleep(2)
        self.__color = 'зелёный'
        print(self.__color)
        sleep(5)

    def off_traffic_light(self):
        self._on = False


my_lighter = TrafficLight()
my_lighter.on_traffic_light()
