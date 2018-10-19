#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : nltk_func.py
# @Author: lucas
# @Date  : 10/18/18
# @Desc  :


import nltk
from nltk.corpus import stopwords
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def download():
    nltk.download()


def tokenize():
    url = 'https://www.python.org/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    soup = BeautifulSoup(html, 'html5lib')
    text = soup.get_text(strip=True)
    tokens = text.split()

    clean_tokens = list()
    st = stopwords.words('english')

    for token in tokens:
        if not token in st:
            clean_tokens.append(token)

    final_tokens = list()
    for item in clean_tokens:
        pprint(item)
        final_tokens.append(item)

    freq = nltk.FreqDist(final_tokens)

    for key, value in freq.items():
        pprint('%s,%s' % (key, value))

    freq.plot(20, cumulative=False)


def run():
    tokenize()


if __name__ == '__main__':
    run()
