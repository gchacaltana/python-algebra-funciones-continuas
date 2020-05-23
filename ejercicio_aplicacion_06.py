# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejercicio de Aplicación 07
__author__ = "Gonzalo Chacaltana"
__version__ = 1.0
from LinearAlgebra.Function import Function
from LinearAlgebra.ContinuousFunction import ContinuousFunction
from LinearAlgebra.CartesianPlane import CartesianPlane
import math


class T(Function):

    def __init__(self, name, x):
        super(T, self).__init__(name, x)
        self.x_min = 0
        self.execute()
        self.validateYi()

    def execute(self, limitTrend=None):
        x = self.getX(limitTrend)
        if (x >= 0 and x <= 30):
            self.yi = 300/(self.xi+3)
        elif (x > 30):
            self.yi = (1.125/((self.xi-5)*(self.xi-15)))+2


if __name__ == '__main__':
    try:
        x = int(input("\nIngresar días de trabajo : "))
        # Instanciamos la función T
        t = T('T', x)
        t.show()

        # Validamos si la función es continua
        fc = ContinuousFunction(t)
        fc.validate()

        # Mostramos el gráfico de la función
        cp = CartesianPlane(t, 100)
        title = "Gráfico de la Función {}(x)".format(t.name)
        label_x = "Dias de trabajo"
        label_y = "Minutos"
        cp.show(title, label_x, label_y)
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
