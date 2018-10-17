#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : qrcode_generator.py
# @Author: lucas
# @Date  : 10/17/18
# @Desc  :

import qrcode


def generate_qrcode(dest_file_path=None, text='https://www.instagram.com/', size=(250, 250)):
    if not dest_file_path:
        return

    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.resize(size).save(dest_file_path)
    img.show()


def run():
    generate_qrcode('qr-code.png')


if __name__ == '__main__':
    run()
