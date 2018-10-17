#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : image_watermark_number.py
# @Author: lucas
# @Date  : 10/17/18
# @Desc  :


from PIL import Image, ImageDraw, ImageFont


def watermark(file_path, text='Great!'):
    image = Image.open(file_path)
    draw = ImageDraw.Draw(image)

    draw.ellipse((40, 0, 50, 10), fill=(255, 0, 0))
    new_font = ImageFont.truetype('Monaco.dfont', 40)  # mac font
    draw.text((200, 100), text, (255, 255, 0), font=new_font)
    image.show()
    image.save('avarta_number.png')


def run():
    watermark(file_path='/Users/lucas/Desktop/avarta.png')


if __name__ == '__main__':
    run()
