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

    def execute(self, limitTrend=None):
        x = self.getX(limitTrend)
        if (x >= 0 and x <= 5):
            self.yi = 15.5-(1.1*self.xi)
        elif (x > 5):
            self.yi = ((5*self.xi) + 45)/(self.xi+2)


if __name__ == '__main__':
    try:
        x = int(input("\nIngresar cantidad de años: "))
        # Instanciamos la función F
        f = F('F', x)
        f.show()

        # Validamos si la función es continua
        fc = ContinuousFunction(f)
        fc.validate()

        # Mostramos el gráfico de la función
        cp = CartesianPlane(f, 50)
        title = "Gráfico de la Función {}(x)".format(f.name)
        label_x = "Impresiones por minuto"
        label_y = "Años"
        cp.show(title, label_x, label_y)
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
