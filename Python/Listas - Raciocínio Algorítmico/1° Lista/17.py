def ler():
    placa = input('Coloque o n° da placa\n>>')
    if len(placa) == 4:
        return print(placa[2]+placa[3])
    else:
        return print('Valor errado')


ler()