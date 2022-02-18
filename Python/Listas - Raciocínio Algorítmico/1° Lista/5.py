def area():
    a = float(input('A\n>> '))
    b = float(input('B\n>> '))
    c = float(input('C\n>> '))
    p = (a+b+c)/2
    t_area = (p*(p-a)*(p-b)*(p-c))**0.5
    return print(f'Área = {t_area}')
area()
# funciona, bate com formuals de sites