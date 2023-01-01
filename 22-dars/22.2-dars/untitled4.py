# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:13:30 2023

@author: Axmadbek
"""
def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')

