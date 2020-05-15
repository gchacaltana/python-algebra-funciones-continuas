# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra import console
import matplotlib.pyplot as plt


class CartesianPlane(object):

    def __init__(self, function: object, range=None):
        self.function = function
        self.range = 15 if range is None else range
        self.coor_x, self.coor_y = [], []
        self.window_width, self.window_height = 16, 10

    def show(self):
        self.showCoordenates()
        self.showGraphic()

    def showCoordenates(self):
        ini = self.function.x - self.range
        end = self.function.x + self.range
        print("\nCalculando {}(x) para {} hasta {}\n".format(
            console.printFunctionName(self.function.name),
            console.printEqualVariable('x', ini),
            console.printEqualVariable('x', end)))

        for n in range(ini, end+1):
            if n >= self.function.x_min:
                self.function.xi = n
                self.function.execute()
                self.coor_x.append(self.function.xi)
                self.coor_y.append(self.function.yi)
                print("{} {} {}({}) = {}".format(
                    console.printEqualVariable('x', self.function.xi),
                    console.printThenSymbol(),
                    console.printFunctionName(self.function.name), self.function.xi, self.function.yi))

    def showGraphic(self):
        plt.style.use('classic')
        fig = plt.figure(figsize=(self.window_width, self.window_height))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.plot(self.coor_x, self.coor_y)
        plt.ylabel("{} (x)".format(self.function.name))
        plt.xlabel("x")
        plt.title('Gráfico de la Función {}'.format(self.function.name))
        plt.show()
