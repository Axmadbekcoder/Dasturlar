#16.2-dars
buxoriy={
    'ism':'Abu abdulloh Muhammad ibn Ismoil',
    'tyil':810,
    'vyil':870,
    'tjoy':'Buxoro',
    'asarlar': 
        ["Al-jome as-sahih", "At-tarix al-kabir", "At-tarix as-sag'ir"]
    }
navoiy={
        'ism':'Alisher Navoiy',
        'tyil':1441,
        'vyil':1501,
        "tjoy":"Xirot",
        'asarlar':['Xamsa', "Lison ut-Tayr", "Mahbub al-Qulub"]
        }
shaxslar=[buxoriy,navoiy]
for shaxs in shaxslar:
    ism=shaxs['ism']
    asarlar=shaxs['asarlar']
    print(f"{ism}ning mashhur asarlari: ")
    for asar in asarlar:
        print(asar)