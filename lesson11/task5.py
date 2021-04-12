# 5. Продолжить работу над первым заданием. Разработайте методы,
# которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

class Warehouse:
    list_of_items = {'Warehouse': []}

    def add(self, place, technics):
        self.list_of_items.setdefault(place, [])
        self.list_of_items[place].append(technics)

    def Print_item(self):
        for i in self.list_of_items:
            print(i)
            for j in self.list_of_items[i]:
                print(f'    {j}')

    def moving(self):
        print("Что нужно переместить(название и модель устройства) ")
        name = input()
        model = input()
        print("Откуда? ")
        place1 = input()
        print("Куда? ")
        place2 = input()

        for key in self.list_of_items:
            if place1 == key:
                for tech in self.list_of_items[key]:
                    if tech.name == name:
                        if tech.model == model:
                            self.list_of_items.setdefault(place2, [])
                            self.list_of_items[place2].append(tech)
                            self.list_of_items[place1].remove(tech)
                            return 0
                print("Такой техники нет")
                return 0
        print("Такого места нет")
        return 0


class OfficeEquip:

    def __init__(self, weight, color, model, price, year_of_issue):
        self.weight = weight
        self.color = color
        self.model = model
        self.price = price
        self.year_of_issue = year_of_issue

    def __str__(self):
        return f'{self.model} {self.color} {self.price} {self.weight} {self.year_of_issue}'


class Printer(OfficeEquip):
    name = 'Printer'

    def __init__(self, weight, color, model, price, year_of_issue, type_printer):
        super().__init__(weight, color, model, price, year_of_issue)
        self.type_printer = type_printer    # Струйный, лазерный


class Scanner(OfficeEquip):
    name = 'Scanner'

    def __init__(self, weight, color, model, price, year_of_issue, type_scanner):
        super().__init__(weight, color, model, price, year_of_issue)
        self.type_scanner = type_scanner    # Ручной, Планшетный, Роликовый


class Xerox(OfficeEquip):
    name = 'Xerox'

    def __init__(self, weight, color, model, price, year_of_issue, type_xerox):
        super().__init__(weight, color, model, price, year_of_issue)
        self.type_xerox = type_xerox    # подвижный, неподвижный


a = Warehouse()
a.add('Warehouse', Printer(123, "Белый", "Samsung", "10000", "2015", "Струйный"))
a.add('Warehouse', Printer(123, "Белый", "Sony", "10000", "2015", "Лазерный"))
a.Print_item()
a.moving()
a.Print_item()

