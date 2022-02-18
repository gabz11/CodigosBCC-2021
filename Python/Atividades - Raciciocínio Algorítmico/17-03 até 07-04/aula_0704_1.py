# q1. dados 3 valores A, B C construa um algoritmo
# q diga se estes valores dos lados podem ser de um triangulo
# e se for diga se é escaleno,equilatero ou isoceles
print('Questão 1.')
# exibe msg
a = int(input('Qual a medida de A?\n>> '))
b = int(input('Qual a medida de B?\n>> '))
c = int(input('Qual a medida de C?\n>> '))
# ^^^^ leitura dos lados A B C
if a > 0 and b > 0 and c > 0 and a < (b + c) and b < (a + c)and c < (a + b):
# condicional para existencia
    # indentação para laço condicional composto
    print(f'O triangulo existe')
    if a == b and b == c:
    # verifica se equilatero
        print(f'Seu triângulo é equilatero(Todos os lados iguais)\n\tDados(A:{a}, B:{b}, C:{c})')
    elif a == b or a == c or b == c:
    # verifica se isosceles
        print(f'Seu triângulo é isósceles(Dois lados iguais)\n\tDados(A:{a}, B:{b}, C:{c})')
    else:
    # se n for os 2 certamente sera escaleno
        print(f'Seu triângulo é escaleno(Todos os lados diferentes)\n\tDados(A:{a}, B:{b}, C:{c})')
else:
    # se n forma triangulo
    print('Não existe')