# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 21:37:15 2022

@author: Axmadbek
"""
def information(ism, familyasi, tyil, tjoy, telefon='', email=''):
    get_info={
        'Ism':ism,
        'Familyasi':familyasi,
        'Tug\'ilgan yil': tyil,
        'Tug\'ilgan joy': tjoy,
        'Telefon raqami': telefon,
        'Elektron pochtasi': email}
    return get_info

print("ma'lumotlarni kiriting.")
malumotlar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    malumotlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break

print("Malumotlar:")
for malumot in malumotlarr:
    print(
        f"{malumot['ism'].title()} {malumot['familiya'].title()},"
        f"{malumot['yoshi']} yoshda, telefoni: {malumot['telefon']}"

