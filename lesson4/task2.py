# Задание 2. Курс Валюты
# Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
# Код валюты может быть в произвольном регистре.
# Функция должна возвращать результат числового типа, например float.
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
# http://www.cbr.ru/scripts/XML_daily.asp.
#
# Выведите на экран курсы для доллара и евро, используя написанную функцию.
#
# Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.


from requests import get, utils


def get_currency_rate(currency):
    currency = currency.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    list_of_content = content.split('<CharCode>')
    for i in list_of_content:
        if currency in i:
            flag1 = i.find('<Value>') + 7
            flag2 = int(i.find('</Value>'))
            currency_rate = i[flag1:flag2]
            currency_rate = (currency_rate.split(','))
            return float('.'.join(currency_rate))
    return None


print(get_currency_rate('UsD'))
print(get_currency_rate('EUr'))