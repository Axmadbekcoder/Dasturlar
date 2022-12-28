#16.5-dars
davlatlar={
    "o'zbekiston":{
        "poytaxti":"toshkent",
        'maydoni':448978,
        'aholi':36_000_000,
        'pul birligi':"so'm"},
    "Rossiya":{
        "poytaxti":"moskva",
        'maydoni':17098246,
        'aholi':144_000_000,
        'pul birligi':"rubl"}}
davlat=input('Davlat nomini kiritng: ').lower()
if davlat in davlatlar:
        info=davlatlar[davlat]
        print(f"\n{davlat}ning poytaxti {info['poytaxti'].title()}"
          f"\nHududi:{info['maydoni']} kv.km"
          f"\nAholisi:{info['aholi']}"
          f"\nPul birligi:{info['pul birligi']}")
else:
    print(f"Bizda {davlat.capitalize()} haqida ma'lumot mavjud emas")