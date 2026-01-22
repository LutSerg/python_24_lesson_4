import datetime
from pprint import pprint

# 1.Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).

email = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam"
}

# 2.Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].

send_date = datetime.datetime.now().strftime('%Y-%m-%d')
email['date'] = send_date

# 3.Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

email['from'] = email['from'].strip().lower()
email['to'] = email['to'].strip().lower()

# 4.Извлеките логин и домен отправителя в две переменные login и domain.
login, domain = email['from'].split('@')

# 5.Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].

email["short_body"] = email['body'][:10] + '...'

# 6. Списки доменов: создайте список личных доменов
# ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
# и список корпоративных доменов
# ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net'].
# с учетом того что там должны быть только уникальные значение

personal_domains = {'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru',
                    'mail.ru',
                    'list.ru', 'bk.ru', 'inbox.ru'}
personal_domains = list(personal_domains)

corporate_domains = {'company.ru', 'corporation.com', 'university.edu', 'organization.org', 'company.ru',
                     'business.net'}
corporate_domains = list(corporate_domains)

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.

crossing = set(personal_domains) & set(corporate_domains)

# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки
# вхождения домена отправителя в список корпоративных доменов.

is_corporate = domain in corporate_domains

# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].

email["clean_body"] = email['body'].replace('\n', ' ').replace('\t', ' ')

# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

email["sent_text"] = f"""Кому: {email['to']},
От {email['from']}
Тема: {email['subject']},
Дата {email['date']}
{email['clean_body']}"""

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет хранится
# что тема письма содержит данные.
is_subject_empty = not email['subject']
is_body_empty = not email['body']

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].

email["masked_from"] = login[:2] + "***@" + domain

#14. Удалите из списка личных доменов значения "list.ru" и "bk.ru"
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

pprint(email)
print(is_corporate, pages, is_subject_empty, is_body_empty)