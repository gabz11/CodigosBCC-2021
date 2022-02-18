def esfera():
    PI = 3.14
    R = float(input('Raio\n>> '))
    V = 4/3*PI*R**3
    A = 4*PI*R**2
    return print(f'Área{A}\nVolume{V}')
esfera()