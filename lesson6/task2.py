# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных
# им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.


spam_count = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_log:
    for line in file_log:
        ip_of_log = line.split()[0]
        if ip_of_log in spam_count:
            spam_count[ip_of_log] += 1
        else:
            spam_count.setdefault(ip_of_log)
            spam_count[ip_of_log] = 1
max_spam = 0
spam_id = ''
for i in spam_count:
    if spam_count[i] > max_spam:
        max_spam = spam_count[i]
        spam_id = i
print(spam_id, max_spam)


