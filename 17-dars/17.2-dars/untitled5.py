savol= "Hurmatli tashrif buyuruvchi yoshingiz nechchida?"
savol +="(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing): "
narx1=2000
narx2=3000
narx3=10000
narx4='bepul'
yosh=''
while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    if yosh<7:
        print(f"Siz muzeyga kirishingiz uchun {narx1} so'm to'lashingiz kerak.")
    elif yosh<18:
        print(f"Siz muzeyga kirishingiz uchun {narx2} so'm to'lashingiz kerak.")
    elif yosh<65:
        print(f"Siz muzeyga kirishingiz uchun {narx3} so'm to'lashingiz kerak.")
    else: 
        print(f"Siz muzeyga kirishingiz uchun {narx4} to'lashingiz kerak.")
        