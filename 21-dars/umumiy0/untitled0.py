# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 10:27:02 2023

@author: Axmadbek
"""
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)