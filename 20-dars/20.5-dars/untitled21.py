# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 22:08:58 2022

@author: Axmadbek
"""
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(10))
        

