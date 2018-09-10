#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : duck_magic.py
# @Author: lucas
# @Date  : 9/10/18
# @Desc  :

from pprint import pprint


class Animal(object):
    def run(self):
        pprint("Animal Running...")


class Cat(Animal):
    def run(self):
        pprint('Cat Running...')


class Dog(Animal):
    def run(self):
        pprint('Dog running..')


class Tortoise(Animal):
    def run(self):
        pprint('Tortoise is Running slowly!')


class Car(object):
    def run(self):
        pprint('Cat Running,not Animal')


class Timer(object):
    def run(self):
        pprint('Timer is Running!')


def run_twice(animal):
    animal.run()
    animal.run()


def run():
    cat = Cat()
    dog = Dog()
    run_twice(cat)
    run_twice(dog)
    run_twice(Tortoise())
    run_twice(Car())
    run_twice(Timer())


if __name__ == '__main__':
    run()
