def circulo():
    R = float(input('Raio\n> '))
    PI = 3.14
    P = 2 * PI * R
    AREA = PI * R ** 2
    D = 2 * R
    return print(f'Área {AREA}\nPerimetro'
                 f' {P}\nDiametro {D}')
circulo()