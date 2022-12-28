#15.3-dars
Restoran={
    'osh':'25000so\'m',
    'non':'4000so\'m',
    'norin':'25000so\'m',
    "manti":"5000so'm",
    "somsa":"7000so'm",
    "shashlikqiyma":"11500so'm",
    "shashlikjigar":"11500so'm",
    "shashlikqirqma":"14000so'm",
    "shashliktovuq":"14000so'm",
    "lag'mon":"18000so'm",
    "sho'rva":"18000so'm"}
print("3 ta taom buyurtma bering:")
buyurtmalar=[]
for n in range(3):
   buyurtmalar.append(input(f"{n+1}-taom:").lower())
    
for buyurtma in buyurtmalar:
    if buyurtma in Restoran:
        print(f"{buyurtma.title()}{Restoran[buyurtma]}")
    else:
            print(f"kechirasiz,bizda {buyurtma} yo'q.")
