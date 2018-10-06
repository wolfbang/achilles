#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : word_count_in_pdf.py
# @Author: lucas
# @Date  : 10/6/18
# @Desc  :


import os
import time
import PyPDF2
from pprint import pprint


def get_page_count(pdf_file):
    """
    need to install PyPDF2 before execute this script
    :param pdf_file: 
    :return: 
    """
    if not os.path.exists(pdf_file):
        return

    with open(pdf_file, 'rb') as f:
        pdf_file_reader = PyPDF2.PdfFileReader(f)
        pages = pdf_file_reader.numPages
        return pages


def extract_data(pdf_file, page):
    if not os.path.exists(pdf_file):
        return

    with open(pdf_file, 'rb') as f:
        pdf_file_reader = PyPDF2.PdfFileReader(f)
        page_object = pdf_file_reader.getPage(page)
        data = page_object.extractText()
        return data


def get_word_count(data):
    if not data:
        return 0

    data = data.split()
    return len(data)


def run():
    pdf_file = '/Users/lucas/Desktop/sample.pdf'
    total_words = 0
    page_count = get_page_count(pdf_file)
    pprint('page_count:{}'.format(page_count))
    for page in range(page_count):
        text = extract_data(pdf_file, page)
        total_words += get_word_count(text)
        pprint((page, total_words))

    time.sleep(1)
    pprint('Total word count:{total_words}'.format(total_words=total_words))


if __name__ == '__main__':
    run()
