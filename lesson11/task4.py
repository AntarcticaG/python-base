# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    list_of_items = []


class OfficeEquip:
    def __init__(self, weight, color, model, price, year_of_issue):
        self.weight = weight
        self.color = color
        self.model = model
        self.price = price
        self.year_of_issue = year_of_issue


class Printer(OfficeEquip):
    def __init__(self, weight, color, model, price, year_of_issue, type_printer):
        super().__init__(weight, color, model, price, year_of_issue)
        self.type_printer = type_printer    # Струйный, лазерный


class Scanner(OfficeEquip):
    def __init__(self, weight, color, model, price, year_of_issue, type_scanner):
        super().__init__(weight, color, model, price, year_of_issue)
        self.type_scanner = type_scanner    # Ручной, Планшетный, Роликовый


class Xerox(OfficeEquip):
    def __init__(self, weight, color, model, price, year_of_issue, type_xerox):
        super().__init__(weight, color, model, price, year_of_issue)
        self.type_xerox = type_xerox    # подвижный, неподвижный

