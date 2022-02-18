# Gabriel Farias | exercício 5 lista 2 r. alg (par/impar)

# cria a função "parimpar"
def parimpar(n):
    # se o resto do modulo da divisão por 2 for igual à 0 o número é par
    if n % 2 == 0:
        # retorna print
        return print(f'{n} é par.')
    # caso ñ é impar
    else:
        # retorna print
        return print(f'{n} é impar.')


num = int(input('Número aqui\n>> '))
parimpar(num)
