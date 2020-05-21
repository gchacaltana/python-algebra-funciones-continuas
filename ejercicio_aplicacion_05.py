# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejercicio de Aplicación 05
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra.Function import Function
from LinearAlgebra.ContinuousFunction import ContinuousFunction
from LinearAlgebra.CartesianPlane import CartesianPlane
import math


class P(Function):

    def __init__(self, name, x):
        super(P, self).__init__(name, x)
        self.x_min = 0
        self.execute()
        self.validateYi()

    def execute(self, limitTrend=None):
        x = self.getX(limitTrend)
        if (x >= 0 and x <= 5):
            self.yi = math.pow(self.xi, 2)
        elif (x > 5):
            self.yi = ((50*self.xi) - 62.5)/((0.5*self.xi)+5)


if __name__ == '__main__':
    try:
        x = int(input("\nIngresar cantidad de minutos : "))
        # Instanciamos la función G
        p = P('P', x)
        p.show()

        # Validamos si la función es continua
        fc = ContinuousFunction(p)
        fc.validate()

        # Mostramos el gráfico de la función
        cp = CartesianPlane(p, 100)
        title = "Gráfico de la Función {}(x)".format(p.name)
        label_x = "Minutos en el organismo"
        label_y = "Peligro de virus"
        cp.show(title, label_x, label_y)
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
