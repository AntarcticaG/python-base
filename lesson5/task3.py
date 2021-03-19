# Задание 3. Генератор объединения двух списков
# Есть два списка:
#
# ```
# tutors = [
#         'Иван', 'Анастасия', 'Петр', 'Сергей',
#         'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#         '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# ```
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей должно быть равно длине списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ```('Станислав', None)```
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.


tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
]
klasses = [
        '9А', '7В', '9Б', '9В', '8Б'
]
def generator_typle(tutors, klasses):
    lenght_lists = len(tutors) - len(klasses)
    for i in range(len(klasses)):
        yield (tutors[i], klasses[i])
    for i in range(lenght_lists):
        yield (tutors[len(klasses)+i], None)

tutors_klasses = generator_typle(tutors,klasses)
print(type(tutors_klasses))
count = 1
for i in range(8):
    print(count, next(tutors_klasses))
    count += 1
