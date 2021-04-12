# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ExceptionZero(Exception):
    pass

def div(a, b):
    if b == 0:
        raise ExceptionZero('ZeroDivisionError')
    return a / b


while True:
    a = int(input('Введите первое число '))
    b = int(input('Введите Второе число '))
    c = ''
    try:
        c = div(a, b)
    except ExceptionZero as err:
        print(err)
    print(c)

