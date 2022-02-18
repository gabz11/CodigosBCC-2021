def cdias():
    anos = int(input('Anos\n>> '))
    meses = int(input('Meses\n>> '))
    dias = int(input('Dias\n>> '))
    total = dias + (meses*30) + (anos*360)
    return print(f'\nViveu o total de {total} dias.')
cdias()