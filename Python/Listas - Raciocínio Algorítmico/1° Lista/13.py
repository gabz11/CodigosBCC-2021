def pg():
    a_1 = float(input('1° termo\n>> '))
    q = float(input('Razão\n>> '))
    n = int(input('Termo\n>> '))
    a_n = a_1*q**(n-1)
    return print(a_n)


pg()
