# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы.


def num_translate_adv(word):
    flag = 0
    if word != word.lower():
        flag = 1
        word = word.lower()
    dic_of_words = {'one':'один', 'two': 'два', 'three':'',
                    'four':'четыре','five':'пять','six':'шесть',
                    'seven':'семь','eight':'восемь','nine':'девять',
                    'ten':'десять'}
    if flag > 0:
        print(dic_of_words[word].title())
    else:
        print(dic_of_words[word])


num_translate_adv('one')

