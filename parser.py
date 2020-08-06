from bs4 import BeautifulSoup
import argparse

import urllib.request
from lxml.html import fromstring
import asyncio
from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
import os
from queue import Queue
from threading import Thread
def all(html):
 doc_tree = BeautifulSoup(html)
 news_list = doc_tree.find_all("div", "item news b-tabloid__topic_news")
 return tuple(f"https://lenta.ru{news.find('a')['href']}" for news in news_list)
 
import pandas as pd
#.read()
def textextract(site):
  response = urllib.request.urlopen(site)
  doc_tree = BeautifulSoup(response)
  tags = doc_tree.find("a", "item dark active")
  tags = tags.get_text() if tags else None
  body = doc_tree.find("div", attrs={"itemprop": "articleBody"})
  if not body:
    raise RuntimeError(f"Article body is not found")

  text = " ".join([p.get_text() for p in body.find_all("p")])

  topic = doc_tree.find("a", "b-header-inner__block")
  topic = topic.get_text() if topic else None

  title = doc_tree.find("h1", attrs={"itemprop": "headline"})
  title = title.get_text() if title else None
  return text
    from datetime import datetime, timedelta
import csv
def logic(start):
    date_start = datetime.strptime(start, '%Y.%m.%d')
    news = []
    text = []
    while date_start<=datetime.today():
      
      
      response = urllib.request.urlopen('https://lenta.ru/'+date_start.strftime("%Y/%m/%d"))
      date_start += timedelta(days=1)
      news += [all(response)]
    for i in range(len(news)):
      for link in news[i]:
        print(link)
        try: 
         text += [(textextract(link))]
        except:
          pass
    return text



text = logic('2020.08.1')
df = pd.DataFrame()
df['text'] = text
gh = df.to_csv('lenta.csv')
 
