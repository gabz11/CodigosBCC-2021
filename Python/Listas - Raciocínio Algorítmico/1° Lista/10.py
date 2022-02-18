def expressar():
    dias = int(input('Sua idade em dias'))
    d_mes = dias/30
    d_ano = dias/360
    return print(f'{dias} dias equivale à {d_mes} meses e {d_ano} anos.')
expressar()
# adotou-se 30 - mes | 360 - ano