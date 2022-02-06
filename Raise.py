# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:25:24 2022

@author: danaf
"""

#Tratamiento de errores Raisee
x="hello"

if not type(x) is int:
    raise TypeError("Solo se permiten numeros enteros")