import datetime
import decimal
from requests import get, utils


def get_currency_rate(currency):
    currency = currency.upper()
    currency_rate = None
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    list_of_content = content.split('<CharCode>')
    date_currency = list_of_content[0][list_of_content[0].find('Date')+6:list_of_content[0].find('Date')+16]
    a = date_currency.split('.')
    day = int(a[0])
    month = int(a[1])
    year = int(a[2])
    date_currency = datetime.date(year, month, day)
    for i in list_of_content:
        if currency in i:
            flag1 = i.find('<Value>') + 7
            flag2 = int(i.find('</Value>'))
            currency_rate = i[flag1:flag2].split(',')
            currency_rate = decimal.Decimal('.'.join(currency_rate))
    return currency_rate, date_currency
