def troco():
    v_pago = int(input('Valor pago\n>> '))
    v_custoproduto = int(input('Preço produto\n>> '))
    return print(f'Troco é {v_custoproduto-v_pago}R$')
troco()