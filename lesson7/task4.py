# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения —
# общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


import os

size_of_file = {}
for i in os.listdir('size_file'):
    path_i = os.path.join('size_file', i)
    statinfo = os.stat(path_i)
    size_i = statinfo.st_size
    key_size = 1
    while size_i:
        print(size_i)
        size_i //= 10
        key_size *= 10
    if key_size in size_of_file.keys():
        size_of_file[key_size] += 1
    else:
        size_of_file.setdefault(key_size, 1)

print(size_of_file)