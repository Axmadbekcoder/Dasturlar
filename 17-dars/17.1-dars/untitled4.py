savol = "Siz yoqtiradigan kitobni kiriting. "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(f"siz yoqtiradigan kitob {qiymat}")