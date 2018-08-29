#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : where_to_eat.py
# @Author: lucas
# @Date  : 8/29/18
# @Desc  :

from Tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', comand=self.quit())
        self.quitButton.pack()


def run():
    app = Application()
    app.master.title('Hello World')
    app.mainloop()


if __name__ == '__main__':
    run()
