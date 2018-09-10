#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : property_decorator.py
# @Author: lucas
# @Date  : 9/10/18
# @Desc  :


class Student(object):
    def __init__(self, score):
        self.score = score

    def __str__(self):
        return str(self.__dict__)

    def get_score(self):
        return self.score

    def s_score(self):
        return self.score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('value must be integer!')

        if score < 0 or score > 100:
            raise ValueError('score must between 0~100,Given:%s' % score)

        self.score = score

    @property
    def secret(self):
        raise AttributeError('secret is not readable!')

    @secret.setter
    def secret(self, secret):
        import base64

        def generate_password_hash(content):
            return str(base64.b64encode(content))

        self.secret_hash = generate_password_hash(secret)


class SuperRectangle(object):
    """
    this rectangle is wrapped with property decorator as a function
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return str(self.__dict__)

    def get_size(self):
        return self.width, self.height

    def set_size(self, size):
        self.width, self.height = size

    def del_size(self):
        del self.width
        del self.height

    size = property(get_size, set_size, del_size, '实例对象')


class Rectangle(object):
    """
    this rectangle is decorated with @property decorator
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return str(self.__dict__)

    @property
    def size(self):
        return self.width, self.height

    @size.setter
    def size(self, size):
        self.width, self.height = size

    @size.getter
    def size(self):
        return self.width, self.height

    @size.deleter
    def size(self):
        del self.height
        del self.width


def run():
    """
    so some basic tests
    :return: 
    """
    student = Student(90)
    print student
    # student.set_score(100)
    print student.score

    rectangle = Rectangle(122, 343)
    print rectangle.size
    rectangle.size = (888, 999)
    print rectangle.size
    del rectangle.width
    print rectangle.height

    # Super Rectangle Test

    super_rectangle = SuperRectangle(333, 444)
    print super_rectangle, dir(super_rectangle)
    perfect_rectangle = SuperRectangle(444, 444)
    print dir(perfect_rectangle), dir(object())

    super_rectangle.size = 12323, 12323
    print super_rectangle

    student.secret = 'my-password'
    print student


if __name__ == '__main__':
    run()
