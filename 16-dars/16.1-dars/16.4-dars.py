#16.4-dars
davlatlar={
    "O'zbekiston":{
        "poytaxti":"toshkent",
        'maydoni':448978,
        'aholi':36_000_000,
        'pul birligi':"so'm"},
    "Rossiya":{
        "poytaxti":"moskva",
        'maydoni':17098246,
        'aholi':144_000_000,
        'pul birligi':"rubl"}}
for davlat, info in davlatlar.items():
    if davlat.lower()=='rossiya':
        davlat=davlat.upper()
    else: davlat=davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxti'].title()}"
          f"\nHududi:{info['maydoni']} kv.km"
          f"\nAholisi:{info['aholi']}"
          f"\nPul birligi:{info['pul birligi']}")