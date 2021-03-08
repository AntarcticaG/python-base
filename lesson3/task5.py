# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков (по одному слову из каждого списка):
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, flag):
    for i in range(count):
        joke = ''
        random_idx_1 = randrange(len(nouns))
        random_idx_2 = randrange(len(adverbs))
        random_idx_3 = randrange(len(adjectives))
        print(nouns[random_idx_1] + ' ' + adverbs[random_idx_2] + ' ' + adjectives[random_idx_3])
        if flag == 1:
            del nouns[random_idx_1]
            del adverbs[random_idx_2]
            del adjectives[random_idx_3]
        if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
            print('Слова для шуток кончились')
            exit()


get_jokes(6,1) # первый аргумент количество шуток, второй разрешение повтора слов, если 1 то слова не повторяются