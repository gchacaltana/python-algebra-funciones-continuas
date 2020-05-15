# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra import console

class Function(object):

    def __init__(self, name, x):
        self.name = name
        self.x, self.y = x, None
        self.xi, self.yi = self.x, None
        self.x_min, self.x_max = None, None

    def validateYi(self):
        if self.yi is None:
            raise Exception(
                "No existe un rango de dominio para el numero ingresado.")
        self.y = self.yi

    def show(self):
        print("\nCuando {} {} {}(x) = {}({}) = {}".format(
            console.printEqualVariable('x', self.x), console.printThenSymbol(),
            console.printFunctionName(self.name), console.printFunctionName(self.name), self.x, self.y))