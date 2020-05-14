# !/usr/bin/env python
# -*- coding: utf-8 -*-

class P(object):

    def __init__(self, x):
        self.x, self.y = x, None
        self.xi, self.yi = self.x, None
        self.is_continous = False
        self.domain = 15
        self.function_execute()
        self.y = self.yi

    def function_execute(self):
        self.function_component_1()
        self.function_component_2()

    def function_component_1(self):
        if (self.xi >= 0 and self.xi <= self.domain):
            self.yi = self.xi/3

    def function_component_2(self):
        if (self.xi > self.domain):
            self.yi = (2*self.xi)/(0.2*self.xi+3)

    def isContinous(self):
        self.calculateLimit()
        self.evaluateFunctionIsContinous()
        return self.is_continous

    def calculateLimit(self):
        self.calculateLimitLeft()
        self.calculateLimitRight()

    def calculateLimitLeft(self):
        self.xi = self.x - 1
        self.function_component_1()
        self.function_component_2()
        self.yLimitLeft = self.yi

    def calculateLimitRight(self):
        self.xi = self.x + 1
        self.function_component_1()
        self.function_component_2()
        self.yLimitRight = self.yi
    
    def evaluateFunctionIsContinous(self):
        if (self.y == self.yLimitLeft == self.yLimitRight):
            self.is_continous = True

    def display(self):
        print("\nCuando x = {}".format(self.x))
        print("P(x) => P({}) = {}".format(self.x, self.y))
        print("\nLa funcion P {} es continua cuando x = {}".format('SI' if self.is_continous else 'No', self.x))


if __name__ == '__main__':
    x = 15
    function = P(x)
    function.display()
