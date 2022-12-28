#15.2-dars
dunyo_davlatlari={
    "AQSh":"Washington D.C.",
    "Italiya":"Rim",
    "Malayziya":"Kuala-lumpur",
    'O\'zbekiston':"Toshkent",
    "Qirg'iziston":"Bishkek",
    "Qozog'iston":"Nursulton",
    "Rossiya":"Moskva",
    "Singapur":"Sungapur",
    "Tojikiston":"Dushanbe",
    }
print("dunyo davlatlari:")
for davlat in sorted(dunyo_davlatlari):
    print(davlat.upper())
    
print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(dunyo_davlatlari.values()):
        print(poytaxt.title())
country=input('qaysi davlatning poytaxtini bilishni hohlaysiz?:')
capital=dunyo_davlatlari.get(country)
if capital==None:
    print('kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")