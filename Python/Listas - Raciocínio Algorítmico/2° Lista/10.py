#   Gabriel Farias  |   Ex 10   Lista 2 |   Divisivel por 5
def divisivel(n):
    # verifica se é divisivel por 5
    if n % 5 == 0:
        # se o resto for 0, é divisivel, retorna print
        return print(f'{n} é divisivel por 5.')
    # caso n for
    else:
        # retorna esse
        return print(f'{n} não é divisivel por 5.')


num = int(input('\n>> '))
divisivel(num)