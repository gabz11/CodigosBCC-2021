#   Gabriel Farias  |   Ex 11 Lista 2   |   Divisivel parte 3
def divisivel(a, b):
    # verifica se um número é divisivel por outro, para isso, o resto deve ser 0
    if a % b == 0:
        # caso for, retorna o seguinte print
        return print(f'{a} é divisivel por {b}')
    # caso não
    else:
        # retorna esse print
        return print(f'{a} não é divisivel por {b}')


num1 = int(input('\n>> '))
num2 = int(input('\n>> '))


divisivel(num1, num2)
