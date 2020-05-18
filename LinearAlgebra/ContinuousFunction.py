# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra import console


class ContinuousFunction(object):

    def __init__(self, function:object):
        self.function = function
        self.is_continuous = False
        self.limitdiff = 0.001

    def validate(self):
        print("\nValidar si la funcion {} es continua.".format(
            console.printFunctionName(self.function.name)))
        self.calculateLimit()
        self.evaluateIsContinuous()
        self.printResult()

    def calculateLimit(self):
        print("\n{}Calculando el Limite de la funcion {}\n".format(
            console.space(2), console.printFunctionName(self.function.name)))
        self.calculateLimitLeft()
        self.calculateLimitRight()

    def calculateLimitLeft(self):
        self.function.execute('-')
        self.function.yLimitLeft = self.function.yi
        print("{}{} {}(x) cuando x -> {} (-) {} {} {}(x) = {}\n".format(
            console.space(2), console.printLimitSymbol(),
            console.printFunctionName(self.function.name),
            self.function.x, console.printThenSymbol(),
            console.printLimitSymbol(),
            console.printFunctionName(self.function.name),
            self.function.yLimitLeft))

    def calculateLimitRight(self):
        self.function.execute('+')
        self.function.yLimitRight = self.function.yi
        print("{}{} {}(x) cuando x -> {} (-) {} {} {}(x) = {}\n".format(
            console.space(2), console.printLimitSymbol(),
            console.printFunctionName(self.function.name),
            self.function.x, console.printThenSymbol(),
            console.printLimitSymbol(),
            console.printFunctionName(self.function.name),
            self.function.yLimitRight))

    def evaluateIsContinuous(self):
        if (self.function.y == self.function.yLimitLeft == self.function.yLimitRight):
            self.is_continuous = True

    def printResult(self):
        message = ('SI' if self.is_continuous else 'No') + " es continua"
        print("\nLa funcion {} {}, cuando {}".format(
            console.printFunctionName(self.function.name),
            console.highlight(message),
            console.printEqualVariable('x', self.function.x)))
