def pa():
    a_1 = float(input('1° termo\n>> '))
    r = float(input('Razão\n>> '))
    termo = int(input('Qual termo?\n>> '))
    a_n = a_1 + (termo - 1) * r
    return print(a_n)


pa()
