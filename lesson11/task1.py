# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


import re

class Date:
    def __init__(self, date):
        self.day, self.month, self.year = self.split_date(date)
        self.validate(date)

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    @classmethod
    def split_date(cls, date):
        _buf = date.split('-')
        day = _buf[0]
        month = _buf[1]
        year = _buf[2]
        return day, month, year

    @staticmethod
    def validate(date):
        pattern = r'(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(\d{4})'
        result = re.findall(pattern, date)
        if len(result) == 0:
            # raise ValueError('Формат неверный')
            print('Формат неверный')
        return result



dates = ['01-10-2020', '11-15-2000', '31-12-2019', '1-9-2000']

for date in dates:
    dt = Date(date)
    print(dt)
