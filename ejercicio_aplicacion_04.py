# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejercicio de Aplicación 04
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
        if (x >= 0 and x < 20):
            self.yi = 0
        elif (x >= 20 and x <= 100):
            self.yi = 0.1*(self.xi)
        elif (x > 100):
            self.yi = ((40*self.xi) - 1000)/((2*self.xi)+100)


if __name__ == '__main__':
    try:
        x = int(input("\nIngresar cantidad de horas : "))
        # Instanciamos la función G
        g = G('G', x)
        g.show()

        # Validamos si la función es continua
        fc = ContinuousFunction(g)
        fc.validate()

        # Mostramos el gráfico de la función
        cp = CartesianPlane(g, 100)
        title = "Gráfico de la Función {}(x)".format(g.name)
        label_x = "Horas de consumo de TV"
        label_y = "Gasto en películas (€ en decenas)"
        cp.show(title, label_x, label_y)
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
