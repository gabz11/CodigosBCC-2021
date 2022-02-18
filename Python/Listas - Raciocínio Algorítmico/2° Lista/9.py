# Gabriel Farias | Ex 9 lista 2 | multiplo de 3
def multiplo(n):
    # para q o número seja multiplo de 3, deve resultar em uma divisão de resto 0
    if n % 3 == 0:
        # caso resulte em 0, retorna print
        return print(f'{n} é multiplo de 3 pois {n} / 3 = {n % 3}')
    else:
        # caso n for, retorna outro print
        return print('Não é múltiplo de 3')


num = int(input('Número aqui\n>> '))
multiplo(num)