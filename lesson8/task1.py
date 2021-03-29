# Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и
# почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?


import re


def email_parse(email_address):
    try:
        email = re.search(r'(\w+)@(\w+\.\w+)', email_address)
        dict_email = dict.fromkeys(['username', 'domain'])
        dict_email['username'] = email.groups()[0]
        dict_email['domain'] = email.groups()[1]
        return dict_email
    except AttributeError:
        return 'ValueError'



print(email_parse('sromanov2001@gmail..com'))
print(email_parse('sromanov@gmail.com'))
print(email_parse('sromanov@gmail.com'))
print(email_parse('sromanovgmail.com'))
print(email_parse('sromanov2001@gmailcom'))


