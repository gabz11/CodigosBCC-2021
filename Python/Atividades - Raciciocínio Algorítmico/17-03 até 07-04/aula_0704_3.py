# q3 equação do 2° grau

a = float(input('\nEntre o valor de a\n>> '))
b = float(input('\nEntre o valor de b\n>> '))
c = float(input('\nEntre o valor de c\n>> '))
delta = (b**2 ) - 4 * a * c
# delta é utilizado para determinar se os valores dados são válidos
if a == 0:
    # a não pode ser 0
    print('\nOBS: O valor de a não pode ser 0.')
elif delta < 0:
    # se delta < 0 não existe raiz real
    print(f'\nNão existem raizes reais pois delta é menor que zero ({delta} < 0)')
else:
    # caso as condicões forem satisfeitas
    # faz a opreação principal
    x1 = (-b + delta ** (1/2))/(2 * a)
    # x1
    x2 = (-b - delta ** (1/2))/(2 * a)
    # x2
    print(f'\nAs raizes são:\nx1 = {x1:.2f}, x2 = {x2:.2f}')
    # exibe a solução