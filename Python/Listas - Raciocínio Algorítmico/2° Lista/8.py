# Gabriel Farias | ex 8 lista 2 | raiz

# func aceita numero real
def checkraiz(n):
    # variavel raiz q pega raiz de n
    raiz = n ** 0.5
    # verifica se é negativa
    if raiz < 0:
        # retorna print
        return print(f'{raiz} é negativo.')
    # verifica se é nula
    elif raiz == 0:
        # retorna print
        return print(f'{raiz} é nula.')
    # verifica se é positiva
    else:
        # retorna print
        return print(f'{raiz} é positivo.')


num = float(input('Número aqui\n>> '))
checkraiz(num)

