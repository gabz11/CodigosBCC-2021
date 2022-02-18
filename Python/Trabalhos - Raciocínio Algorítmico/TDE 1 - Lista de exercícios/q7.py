# Questão 7.
print('Questão 7')
# exibe operação do programa
while True:
    # laço while para sempre rodar programa até q usuario entre entrada no prompt para terminar
    print('\nCalculo de equação do 2° grau.(Bhaskara)\n1. Iniciar\n2. Sair')
    # print mostrando as operações principais
    prompt = input('\nSelecione uma opção\n>> ')
    # prompt para entrada e selecionar operação
    if prompt =='1':
        # condicional para operação principal
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
    elif prompt =='2':
        # condicional para encerrar o programa
        print('\nFIM')
        # exibe mensagem
        quit()
        # finaliza program com codigo 0
    else:
        # caso o usuário entre um prompt invalido, exibe tal mensagem.
        print('\nComando Invalido: Por favor selecione uma das opções')