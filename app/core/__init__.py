#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: lucas
# @Date  : 8/4/18
# @Desc  :

from . import db_setting
from app.base import module as a_module


def base_module_run():
    a_module.run()
