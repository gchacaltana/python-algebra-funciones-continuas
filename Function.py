# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Function(object):

    def __init__(self, name, x):
        self.name = name.upper()
        self.x, self.y = x, None
        self.xi, self.yi = self.x, None
        self.is_continous = False

    def validateYi(self):
        if self.yi is None:
            raise Exception(
                "No existe un rango de dominio para el numero ingresado.")
        self.y = self.yi

    def execute(self):
        pass

    def function_component_1(self):
        pass

    def function_component_2(self):
        pass

    def validateContinous(self):
        print("Validar si la funcion {} es continua.".format(self.name))
        self.calculateLimit()
        self.evaluateFunctionIsContinous()
        print("\nLa funcion {} {} es continua cuando x = {}".format(
            self.name, 'SI' if self.is_continous else 'No', self.x))

    def calculateLimit(self):
        print("Calculando el Limite de la funcion {}".format(self.name))
        self.calculateLimitLeft()
        self.calculateLimitRight()

    def calculateLimitLeft(self):
        self.xi = self.x - 1
        print("Lim {}(x) cuando x se aproxima a {} por la izquierda".format(
            self.name, self.x))
        self.function_component_1()
        self.function_component_2()
        self.yLimitLeft = self.yi
        print("Lim {}(x) = {}".format(self.name, self.yLimitLeft))

    def calculateLimitRight(self):
        self.xi = self.x + 1
        print("Lim {}(x) cuando x se aproxima a {} por la derecha".format(
            self.name, self.x))
        self.function_component_1()
        self.function_component_2()
        self.yLimitRight = self.yi
        print("Lim {}(x) = {}".format(self.name, self.yLimitRight))

    def evaluateFunctionIsContinous(self):
        if (self.y == self.yLimitLeft == self.yLimitRight):
            self.is_continous = True

    def display(self):
        print("\nCuando x = {}".format(self.x))
        print("{}(x) => {}({}) = {}".format(
            self.name, self.name, self.x, self.y))

    def displayCoordinates(self, interval):
        ini = self.x - interval
        end = self.x + interval
        print("\nMostrando {}(x) para el rango de x de {} a {}\n".format(
            self.name, ini, end))
        for n in range(ini, end):
            self.xi = n
            self.execute()
            print("x = {} => {}({}) = {}".format(
                self.xi, self.name, self.xi, self.yi))
