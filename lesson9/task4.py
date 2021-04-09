#  Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw() (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры каждого класса и положить их в список.
# Проитерироваться по этому списку и вызвать метод draw() для каждого элемента.


class Stationary:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        print("уникальное сообщение для ручки")


class Pencil(Stationary):
    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        print("уникальное сообщение для карандаша")


class Handle(Stationary):
    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        print("уникальное сообщение для маркера")


stationary_list = [Stationary(), Pen(), Pencil(), Handle()]
for stationary in stationary_list:
    stationary.draw()
