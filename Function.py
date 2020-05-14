# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0


class Function(object):

    def __init__(self, name, x):
        self.name = name.upper()
        self.x, self.y = x, None
        self.xi, self.yi = self.x, None
        self.is_continous = False
        self.consoleConfig()

    def validateYi(self):
        if self.yi is None:
            raise Exception(
                "No existe un rango de dominio para el numero ingresado.")
        self.y = self.yi

    def consoleConfig(self):
        self.symbol_then = "\033[94m => \033[0m"
        self.name = "\033[92m" + self.name + "\033[0m"

    def execute(self):
        pass

    def function_component_1(self):
        pass

    def function_component_2(self):
        pass

    def validateContinous(self):
        print("\nValidar si la funcion {} es continua.".format(self.name))
        self.calculateLimit()
        self.evaluateFunctionIsContinous()
        print("\nLa funcion {} \033[93m{} es continua\033[0m, cuando x = {}".format(
            self.name, 'SI' if self.is_continous else 'No', self.x))

    def calculateLimit(self):
        print("\n{}Calculando el Limite de la funcion {}\n".format(
            ''.ljust(2), self.name))
        self.calculateLimitLeft()
        self.calculateLimitRight()

    def calculateLimitLeft(self):
        self.xi = self.x - 1
        self.function_component_1()
        self.function_component_2()
        self.yLimitLeft = self.yi
        print("{}Lim {}(x) cuando x -> {} (-) {} Lim {}(x) = {}\n".format(
            ''.ljust(2), self.name, self.x, self.symbol_then, self.name, self.yLimitLeft))

    def calculateLimitRight(self):
        self.xi = self.x + 1
        self.function_component_1()
        self.function_component_2()
        self.yLimitRight = self.yi
        print("{}Lim {}(x) cuando x -> {} (+) {} Lim {}(x) = {}".format(
            ''.ljust(2), self.name, self.x, self.symbol_then, self.name, self.yLimitRight))

    def evaluateFunctionIsContinous(self):
        if (self.y == self.yLimitLeft == self.yLimitRight):
            self.is_continous = True

    def display(self):
        print("\nCuando \033[93m x = {} \033[0m {} {}(x) = {}({}) = {}".format(
            self.x, self.symbol_then, self.name, self.name, self.x, self.y))

    def displayCoordinates(self, interval):
        ini = self.x - interval
        end = self.x + interval
        print("\nMostrando {}(x) para el rango de valores de x ({} a {})\n".format(
            self.name, ini, end))
        for n in range(ini, end+1):
            self.xi = n
            self.execute()
            print("x = {} => {}({}) = {}".format(
                self.xi, self.name, self.xi, self.yi))
