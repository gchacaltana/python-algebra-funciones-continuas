# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra.Function import Function
from LinearAlgebra.ContinuousFunction import ContinuousFunction
from LinearAlgebra.CartesianPlane import CartesianPlane


class F(Function):

    def __init__(self, name, x):
        super(F, self).__init__(name, x)
        self.x_min = 0
        self.execute()
        self.validateYi()

    def execute(self):
        if (self.xi >= 0 and self.xi <= 5):
            self.yi = 15.5-(1.1*self.xi)
        elif (self.xi > 5):
            self.yi = ((5*self.xi) + 45)/(self.xi+2)


if __name__ == '__main__':
    try:
        x = int(input("\nIngresar cantidad de años: "))
        f = F('F', x)
        f.show()
        fc = ContinuousFunction(f)
        fc.validate()
        cp = CartesianPlane(f, 50)
        cp.show()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
