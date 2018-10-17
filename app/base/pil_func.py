#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pil_func.py
# @Author: lucas
# @Date  : 10/16/18
# @Desc  :


from PIL import Image, ImageDraw, ImageFont
from pprint import pprint


def show(file_path):
    image = Image.open(file_path).convert('RGBA')
    txt = Image.new('RGBA', image.size, (0, 0, 0, 0))
    out = Image.alpha_composite(image, txt)
    out.show()


def thumbnail(file_path, dest_file_path, size=(128, 128)):
    try:
        image = Image.open(file_path)
        image.thumbnail(size)
        image.save(dest_file_path, 'jpeg')
    except IOError as e:
        pprint('ERROR: %s,%s,error msg:%s' % (file_path, dest_file_path, e))


def run():
    thumbnail(file_path='/Users/lucas/Desktop/test.jpg', dest_file_path='/Users/lucas/Desktop/test_result.jpg')


if __name__ == '__main__':
    run()
