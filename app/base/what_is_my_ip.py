#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : what_is_my_ip.py
# @Author: lucas
# @Date  : 10/5/18
# @Desc  :


import requests
from pprint import pprint


def query_ip():
    url = 'http://ip-api.com/json'
    json_result = requests.get(url)
    data = json_result.json()
    pprint(data)

    ip = data['query']
    country_code = data['country']
    country = data['country']
    city = data['city']
    timezone = data['timezone']

    pprint('{ip}'.format(ip=ip))
    pprint('{country_code}'.format(country_code=country_code))
    pprint('{country}'.format(country=country))
    pprint('{city}'.format(city=city))
    pprint('{timezone}'.format(timezone=timezone))


def run():
    query_ip()


if __name__ == '__main__':
    run()
