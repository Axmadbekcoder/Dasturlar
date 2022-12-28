#16.1-dars
buxoriy={
    'ism':'Abu abdulloh Muhammad ibn Ismoil',
    'tyil':810,
    'vyil':870,
    'tjoy':'Buxoro'
    }
navoiy={
        'ism':'Alisher Navoiy',
        'tyil':1441,
        'vyil':1501,
        "tjoy":"Xirot"
        }
shaxslar=[buxoriy,navoiy]
for shaxs in shaxslar:
    ism=shaxs['ism']
    tyil=shaxs['tyil']
    vyil=shaxs['vyil']
    tjoy=shaxs['tjoy']
    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan."
          f"{vyil-tyil} yil umr ko'rgan.")