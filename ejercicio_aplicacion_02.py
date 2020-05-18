# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra.Function import Function
from LinearAlgebra.ContinuousFunction import ContinuousFunction
from LinearAlgebra.CartesianPlane import CartesianPlane


class P(Function):

    def __init__(self, name, x):
        super(P, self).__init__(name, x)
        self.x_min = 0
        self.execute()
        self.validateYi()

    def execute(self, limitTrend=None):
        x = self.getX(limitTrend)
        if (x >= 0 and x <= 15):
            self.yi = self.xi/3
        elif (x > 15):
            self.yi = (2*self.xi)/((0.2*self.xi)+3)


if __name__ == '__main__':
    try:
        x = int(input("Ingresa las horas de estudio: "))
        p = P('P', x)
        p.show()
        fc = ContinuousFunction(p)
        fc.validate()
        cp = CartesianPlane(p, 50)
        cp.show()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
