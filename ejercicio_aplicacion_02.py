# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Function import Function

class P(object):

    def __init__(self, name, x):
        self.function = Function(name, x)
        self.execute()
        self.function.validateYi()

    def execute(self):
        self.function_component_1()
        self.function_component_2()

    def function_component_1(self):
        if (self.function.xi >= 0 and self.function.xi <= 15):
            self.function.yi = self.function.xi/3

    def function_component_2(self):
        if (self.function.xi > 15):
            self.function.yi = (2*self.function.xi)/(0.2*self.function.xi+3)


if __name__ == '__main__':
    try:
        x = int(input("Ingresa el valor de x: "))
        p = P('P', x)
        p.function.display()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
