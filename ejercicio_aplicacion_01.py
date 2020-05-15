# !/usr/bin/env python
# -*- coding: utf-8 -*-

from LinearAlgebra.Function import Function
from LinearAlgebra.ContinuousFunction import ContinuousFunction
from LinearAlgebra.CartesianPlane import CartesianPlane


class G(Function):

    def __init__(self, name, x):
        super(G, self).__init__(name, x)
        self.x_min = 0
        self.execute()
        self.validateYi()

    def execute(self):
        if (self.xi >= 0 and self.xi <= 100):
            self.yi = (0.02*self.xi)-1
        elif (self.xi > 100):
            self.yi = (30*self.xi)/(2*self.xi+2300)


if __name__ == '__main__':
    try:
        x = int(input("\nIngresa el valor de X: "))
        g = G('G', x)
        g.show()

        fc = ContinuousFunction(g)
        fc.validate()
        cp = CartesianPlane(g, 80)
        cp.show()

    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
