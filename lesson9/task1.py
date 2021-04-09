# Создать класс TrafficLight (светофор).
# определить у него один приватный атрибут color (цвет)
# и метод get_current_signal() (получить текущий цвет);
# после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью:
# красный (3 сек), жёлтый (1 сек), зелёный (3 сек);
# переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
# проверить переключение режимов работы светофора,
# опрашивая в цикле текущее состояние светофора с интервалом 0.5 секунды,
# используя метод get_current_signal().

from datetime import datetime
import time


class TrafficLight:

    __color = None

    def __init__(self):
        self.__color = ['red', 'yellow', 'green']
        self.start = datetime.now()

    def get_current_signal(self):
        self.time_working = (datetime.now() - self.start).total_seconds()
        if self.time_working - 7 * (self.time_working // 7) > 4:
            print(self.__color[2], self.time_working)
        elif self.time_working - 7 * (self.time_working // 7) > 3:
            print(self.__color[1], self.time_working)
        elif self.time_working - 7 * (self.time_working // 7) > 0:
            print(self.__color[0], self.time_working)


a = TrafficLight()

while True:
    a.get_current_signal()
    time.sleep(0.5)



