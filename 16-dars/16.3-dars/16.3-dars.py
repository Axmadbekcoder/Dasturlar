#16.3-dars
kinolar={
    "Bahtiyor":['marvel', 'qahramonlar'],
    "Zohidjon":['vatan','stalingrad'],
    'Eldor':['sniper','sardor'],
    'MuhammadAli':['merlin','kelajakka qaytib']}
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)
