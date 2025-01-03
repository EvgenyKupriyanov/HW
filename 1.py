from lxml import html
import requests
from pprint import pprint
import pandas as pd
import csv

url = 'https://news.mail.ru/'
response = requests.get(url)
dom = html.fromstring(response.text)
list_news = []
top = {}
mid = {}
news = {}

top_news = dom.xpath('//div[@class="d1349e4e3f dbc6642ba6 eb47cfc341"]/text()')
top_text = dom.xpath('//div[@class="cca994f104 e354599ff8"]/span/text()')
print(top_news)
print(top_text)
top['top_news'] = top_news
list_news.append(top)

mid_news = dom.xpath('//div[@class="c03cd1278e"]/div/a/span/text()')
print(mid_news)
mid['mid_news'] = mid_news
list_news.append(mid)

new = dom.xpath('//div[@class="d60c83730a"]/div/a/span/text()')
print(new)
news['news'] = new
list_news.append(news)

print(list_news)

df = pd.DataFrame(list_news)
df.to_csv('new.csv')

with open('news.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(list_news)

