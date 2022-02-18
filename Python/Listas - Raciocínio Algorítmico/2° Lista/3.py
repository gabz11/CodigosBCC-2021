def imprimir(n):
    # verifica se a variavel n é maior q 20
    if n > 20:
        # imprime o numero
        return n
    # caso não faz o seguinte
    else:
        # não imprime o número
        return 'Null'


# entrada do numero com input
num = int(input('Entre um número\n>> '))
# chama a função imprimir() com o argumento num, como n esta associada a nenhuma variavel, deve se imprimir para ver
# o resultado
print(imprimir(num))
