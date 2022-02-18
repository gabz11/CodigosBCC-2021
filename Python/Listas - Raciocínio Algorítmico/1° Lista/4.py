def kilos():
    v_kgproduto = int(input('Valor do produto por kilo\n>> '))
    v_totalkilos = int(input('Kilos para comprar do produto\n>> '))
    total = v_totalkilos*v_kgproduto
    return print(f'O total pago é {total}R$')
kilos()