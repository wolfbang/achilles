#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : robot.py
# @Author: lucas
# @Date  : 9/4/18
# @Desc  :


class Robot(object):
    population = 0

    def __init__(self, name):
        self.name = name
        import pprint
        pprint.pprint('{name} Initializing.'.format(name=name))
        Robot.population += 1

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def die(self):
        """I'm dying!"""
        print '{name} is being destroyed!'.format(name=self.name)
        Robot.population -= 1
        if Robot.population == 0:
            print '{name} is the last one!'.format(name=self.name)
        else:
            print 'there are still {number} working!'.format(number=Robot.population)

    def say_hi(self):
        import pprint
        pprint.pprint('hello,my master call me {name}'.format(name=self.name))

    @classmethod
    def how_many(cls):
        print 'we have {population} robot(s)'.format(population=Robot.population)
        return Robot.population


def run():
    megatron = Robot('Megatron')
    blaster = Robot('Blaster')
    print megatron
    Robot.how_many()
    megatron.die()
    Robot.how_many()
    blaster.die()
    Robot.how_many()


if __name__ == '__main__':
    run()
