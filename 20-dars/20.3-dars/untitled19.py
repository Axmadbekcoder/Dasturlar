# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 21:57:38 2022

@author: Axmadbek
"""
def son(x,y,z):
    if x>y>z or x>z>y:
        a=x
    elif y>x>z or y>z>x:
        a=y
    elif z>x>y or z>y>x:
        a=z
    return a

