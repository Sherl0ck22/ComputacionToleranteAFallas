# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:19:10 2022

@author: danaf
"""

#Tratamiento de errores try except name error
try:
    print(x)
except NameError:
    print("La variable no esta definida")
except:
    print("Ha ocurrido un error")