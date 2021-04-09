# Реализовать базовый класс Employee (сотрудник).
# определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
# создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
# income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# в классе Position реализовать методы получения полного имени сотрудника get_full_name()
# и дохода с учётом премии get_total_income() (wage + bonus);
# проверить работу примера на реальных данных: создать экземпляры классов Employee,
# Position, вывести на экран имя сотрудника, его должность и вознаграждение сотрудника,
# используя методы класса Position.


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position:

    _income = None

    def __init__(self, employee, position, income):
        self.employee = employee
        self.position = position
        self._income = income

    def get_full_name(self):
        print(self.employee.name, self.employee.surname)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])



position1 = Position(Employee('Александр', 'Романов'),
                     'программист',
                     {'wage': 100000, 'bonus': 19999})

position1.get_full_name()
position1.get_total_income()
