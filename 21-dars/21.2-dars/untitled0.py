# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 10:27:02 2023

@author: Axmadbek
"""
def katta_harf(matnlar):
    matnlar=matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()  
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
yangi_ismlar=katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)