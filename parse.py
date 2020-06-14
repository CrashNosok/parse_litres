import requests
from bs4 import BeautifulSoup as BS
import re
import datetime

text = ''
now = datetime.datetime.today()
year = now.year
city = input('Введите название города: ').strip().capitalize()

date_w = input('Введите дату в формате мм-дд\n'
               'для просмотра погоды на сегодняшний день, ничего не вводите: ').strip()

if date_w:
    match = re.match(r'\d{2}-\d{2}', date_w)
    if not match:
        print('Incorect date formst')
        exit()
    date_w = f'{year}-{date_w}'
else:
    date_w = now.strftime('%Y-%m-%d')

url = f'https://sinoptik.ua/погода-{city}/{date_w}'
r = requests.get(url)
html = BS(r.content, 'html.parser')
title = html.find('title').text
if title.find('404') != -1:
    print('Error 404')
    exit()
el = html.select('#content')[0]
date = el.select('.date')[0].text
t_min = el.select('.temperature .min')[0].text
t_max = el.select('.temperature .max')[0].text
description = el.select('.wDescription .description')[0].text.strip()

if date_w:
    text = f'{city} погода на {date_w}. Число сегодня: {date}\nТемпература: {t_min} {t_max}\n{description}'
print(text)
