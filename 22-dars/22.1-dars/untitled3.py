# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:53:30 2023

@author: Axmadbek
"""
def kopaytma(*sonlar):
    kopaytirish=1
    for son in sonlar:
        kopaytirish*=son
    return kopaytirish


