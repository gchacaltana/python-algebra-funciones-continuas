# !/usr/bin/env python
# -*- coding: utf-8 -*-

class G(object):

    def __init__(self, x):
        self.x, self.y = x, None
        self.xi, self.yi = self.x, None
        self.is_continous = False
        self.function_execute()
        self.y = self.yi

    def function_execute(self):
        self.function_component_1()
        self.function_component_2()

    def function_component_1(self):
        if (self.xi >= 0 and self.xi <= 100):
            self.yi = (0.02*self.xi)-1

    def function_component_2(self):
        if (self.xi > 100):
            self.yi = (30*self.xi)/(2*self.xi+2300)

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
        print("Cuando x = {}".format(self.x))
        print("G(x) => G({}) = {}".format(self.x, self.y))
        print("La funcion G {} es continua cuando x = {}".format('SI' if self.is_continous else 'No', self.x))

    def displayCoordinates(self, interval):
        ini = self.x - interval
        end = self.x + interval
        for n in range(ini,end):
            self.xi = n
            self.function_execute()
            print("x = {} => G({}) = {}".format(self.xi,self.xi,self.yi))

if __name__ == '__main__':
    x = 100
    function = G(x)
    function.display()
    function.displayCoordinates(5)
