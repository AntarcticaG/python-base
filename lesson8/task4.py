# 4. Написать декоратор с аргументом-функцией (callback), позволяющий
# валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?


from functools import wraps


def val_checker(callback):
    @wraps(callback)
    def valid(*args):
        if not isinstance(*args, int):
            raise ValueError(*args)

        res = callback(*args)
        return res
    return valid



@val_checker
def calc_cube(x):
    return x ** 3

result = calc_cube(5)
print(result)
result = calc_cube('565')
print(result)


