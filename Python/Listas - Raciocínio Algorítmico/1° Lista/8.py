def euclides():
    x_1 = float(input('x1\n>> '))
    y_1 = float(input('y1\n>> '))
    x_2 = float(input('x2\n>> '))
    y_2 = float(input('y2\n>> '))
    dist = ((y_2-y_1)**2 + (x_2-x_1)**2)**0.5
    return print(f'Distância: {dist}')
euclides()