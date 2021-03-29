# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>

from functools import wraps


def type_logger(func):
    print(func)

    @wraps(func)
    def decor_logger(*args):
        res = func(*args)
        print(*args, type(*args))
        return res
    return decor_logger


@type_logger
def calc_cube(x):
    return x ** 3


cube = calc_cube(5)
print(cube)

# Не  знаю как сделать для нескольких переменных


