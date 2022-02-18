# Gabriel Farias | ex 6 lista 2 | pos, neg ou nulo


# recebe numero real como argumento
def verifica(n):
    # verifica se é negativo
    if n < 0:
        # caso for retorna
        return print(f'{n} é negativo.')
    # verifica se é nulo
    elif n == 0:
        # caso sim retorna
        return print(f'{n} é nulo.')
    # caso n for negativo ou nulo, resta apenas positivos
    else:
        # caso s, retorna
        return print(f'{n} é positivo.')


num = float(input('Coloque o número\n>> '))
verifica(num)
