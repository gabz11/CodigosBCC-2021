def ler():
    placa = input('Número da placa\n>> ')
    if len(placa) == 4:
        return print(placa[3])
    else:
        return print('Valor invalido')


ler()