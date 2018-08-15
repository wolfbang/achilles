#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : magics.py
# @Author: lucas
# @Date  : 8/10/18
# @Desc  :


import logging

logging.basicConfig(filename='/Users/lucas/projects/achilles/log.log', filemode='wb', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def run():
    print('python is fun!')
    message = 'sequence_id=%s,random_id=%s' % ('888','999')
    print(message)
    logger.info(message)
    logger.info(message)
    logger.info("{0}".format("get busy living!"))
    pass


if __name__ == '__main__':
    run()
