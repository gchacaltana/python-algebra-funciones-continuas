# !/usr/bin/env python
# -*- coding: utf-8 -*-

from Function import Function

class G(object):

    def __init__(self, name, x):
        self.function = Function(name,x)
        self.execute()
        self.function.validateYi()

    def execute(self):
        self.function_component_1()
        self.function_component_2()

    def function_component_1(self):
        if (self.function.xi >= 0 and self.function.xi <= 100):
            self.function.yi = (0.02*self.function.xi)-1

    def function_component_2(self):
        if (self.function.xi > 100):
            self.function.yi = (30*self.function.xi)/(2*self.function.xi+2300)

if __name__ == '__main__':
    x = 15
    try:
        g = G('G', x)
        g.function.display()
        g.function.validateContinous()
        g.function.displayCoordinates(5)
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
