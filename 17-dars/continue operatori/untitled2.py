# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 18:51:01 2022

@author: Vosem
"""

sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")