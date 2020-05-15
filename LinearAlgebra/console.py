# !/usr/bin/env python
# -*- coding: utf-8 -*-
from LinearAlgebra import constants

def printFunctionName(name:str):
    return constants.COLOR_GREEN + name + constants.END_COLOR

def printEqualVariable(variableName:str, variableValue:int):
    return constants.COLOR_YELLOW + variableName + " = " + str(variableValue) + constants.END_COLOR

def printThenSymbol():
    return constants.COLOR_BLUE + " => " + constants.END_COLOR

def space(length:int):
    return ''.ljust(length)

def highlight(message:str):
    return constants.COLOR_YELLOW + message + constants.END_COLOR

def printLimitSymbol():
    return constants.COLOR_YELLOW + "Lim" + constants.END_COLOR