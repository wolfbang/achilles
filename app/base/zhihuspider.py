#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zhihuspider.py
# @Author: lucas
# @Date  : 8/3/18
# @Desc  :


import os
import requests
from lxml import html

headers = {

    'Host': 'www.zhihu.com',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


def save(text, filename='temp', path='/Users/lucas/Temp/download/'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'w') as f:
        print 'output:', fpath
        f.write(text)


def save_image(image_url):
    resp = requests.get(image_url)
    page = resp.content
    filename = str(image_url).split("zhimg.com/")[-1]
    save(page, filename)


def crawl(url):
    resp = requests.get(url, headers=headers)
    page = resp.content
    print page
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@data-original]/@data-original')
    for image_url in image_urls:
        print 'image_url:', image_url
        save_image(image_url)


if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/27364360'  # 有一双美腿是一种怎样的体验?
    url = 'https://www.zhihu.com/question/277582435/answer/394438239'
    url = u'https://www.zhihu.com/question/286121246'
    crawl(url)
