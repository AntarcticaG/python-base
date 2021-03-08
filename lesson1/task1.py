# Человеко-ориентированное представление интервала времени
# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек

sec = minute = hour = day = 0
sec = int(input("Введите интервал в секундах: "))
if sec >= 60:
    minute = sec // 60
    sec = sec % 60
if minute >= 60:
    hour = minute // 60
    minute = minute % 60
if hour >= 24:
    day = hour // 24
    hour = hour % 24

if day == 0 and hour == 0 and minute == 0:
    print(sec, "сек")
elif day == 0 and hour == 0:
    print(minute, "мин", sec, "сек")
elif day == 0:
    print(hour, "час", minute, "мин", sec, "сек")
else:
    print(day, "дн", hour, "час", minute, "мин", sec, "сек")