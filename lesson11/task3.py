# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class ExceptionDigit(Exception):
    def __init__(self, stop_word):
        self.word = stop_word


def valid(a):
    try:
        return int(a)
    except ValueError:
        raise ExceptionDigit(a)


list = []
while True:
    try:
        a = input()
        valid(a)
        list.append(a)
    except ExceptionDigit:
        if a == 'stop':
            break
        print('Число введи, дуреха')
print(list)
