# !/usr/bin/env python
# -*- coding: utf-8 -*-

class P(object):

    def __init__(self, x):
        self.x = x

    def display(self):
        print("dummy response")


if __name__ == '__main__':
    x = 15
    function = P(x)
    function.display()
