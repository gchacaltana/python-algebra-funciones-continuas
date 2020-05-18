# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra.Function import Function
from LinearAlgebra.ContinuousFunction import ContinuousFunction
from LinearAlgebra.CartesianPlane import CartesianPlane


class G(Function):

    def __init__(self, name, x):
        super(G, self).__init__(name, x)
        self.x_min = 0
        self.execute()
        self.validateYi()

    def execute(self, limitTrend=None):
        x = self.getX(limitTrend)
        if (x >= 0 and x <= 100):
            self.yi = (0.02*self.xi)-1
        elif (x > 100):
            self.yi = (30*self.xi)/(2*self.xi+2300)


if __name__ == '__main__':
    try:
        x = int(input("\nIngresa el valor de X: "))
        # Instanciamos la función G
        g = G('G', x)
        g.show()

        # Validamos si la función es continua
        fc = ContinuousFunction(g)
        fc.validate()
        
        # Mostramos el gráfico de la función
        cp = CartesianPlane(g, 80)
        cp.show()

    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
