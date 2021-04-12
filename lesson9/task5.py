# Реализуйте базовый класс Car.
# при создании класса должны быть переданы атрибуты: color (str), name (str).
# реализовать в классе методы: go(speed), stop(), turn(direction), которые должны изменять состояние машины -
# для хранения этих свойств вам понадобятся дополнительные атрибуты - придумайте какие.
# добавьте метод is_police() - который возвращает True/False,
# в зависимости от того является ли этот автомобиль полицейским (см.дальше)
# Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
# Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки
# название, цвет, текущую скорость автомобиля и направление движения (в случае если автомобиль едет),
# для полицейских автомобилей перед названием автомобиля должно идти слово POLICE;
# Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости должна выводиться фраза
# "ПРЕВЫШЕНИЕ!", если скорость превышает 60 (TownCar) и 40 (WorkCar).
# Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций,
# для каждого автомобиля сделайте одно из случайных действий: go, stop, turn со случайными параметрами.
# После каждого действия показывайте статус автомобиля.


import random


class Car:

    speed = 90
    direction_var = ['Вперед', 'Назад', "Влево", "Вправо"]
    direction = ''
    excess = ''
    speed_limit = 10000

    def __init__(self, color, name):
        self.color = color
        self.name = name
        if self.is_police():
            self.police = "POLICE"
        else:
            self.police = ''

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = self.direction_var[direction]

    def is_police(self):
        return False

    def get_status(self):
        if self.speed > self.speed_limit:
            self.excess = "ПРЕВЫШЕНИЕ!"
        if self.speed > 0:

            return f'{self.police} {self.color} {self.name} {self.speed} {self.excess} {self.direction}'
        else:
            return f'{self.police} {self.color} {self.name} Стоит'


class TownCar(Car):
    speed_limit = 60


class SportCar(Car):
    speed_limit = 90


class WorkCar(Car):
    speed_limit = 60


class PoliceCar(Car):
    def is_police(self):
        return True


car1 = TownCar("Белый", "Мерс")
car2 = SportCar("Синий", "Ламборгини")
car3 = WorkCar("Желтый", "Автобус")
car4 = PoliceCar("Черный", "Порше")

car_list = [car1, car2, car3, car4]

for i in range(10):
    for car in car_list:
        action = random.randint(1, 3)
        if action == 1:
            car.go(random.randint(10, 150))
        elif action == 2:
            car.turn(random.randint(0, 3))
        elif action == 3:
            car.stop()
        print(car.get_status())
    print('===================')







