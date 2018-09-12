#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : class_type.py
# @Author: lucas
# @Date  : 9/10/18
# @Desc  :


from app.core.model.property_decorator import Student


def run():
    student = Student(90)
    print student
    a_list = [1, 2, 4, 89]
    print 'isinstance(a_list,list)=', isinstance(a_list, list)
    print 'isinstance(student, Student)=', isinstance(student, Student)
    print 'isinstance(109, int)', isinstance(109, int)
    print 'isinstance((109, \'name\'), set)=', isinstance((109, 'name'), set)
    print 'isinstance({},dict)=', isinstance({}, dict)


if __name__ == '__main__':
    run()
