# Q1 - progressão arítmética P.A
print('Questão 1')
while True:
    # Laço while para programa sempre executar até q usuário termine com o comando de sair
    print('Calculo para descobrir termo de uma P.A\n1. Calcular\n2. Sair\n')
    # exibe possiveis operações do programa
    prompt = input('\nDigite sua opção\n>> ')
    # le a entrada do usuário
    if prompt == '1':
        # condicional principal
        # calcula ax de uma p.a com os dados fornecidos pelo usuário
        a1 = float(input('\nEntre o valor do primeiro termo(a1)\n>> '))
        # primeiro termo
        r = float(input('\nEntre o valor da razão(r)\n>>'))
        # razão
        n = int(input('\nQual termo da P.A você gostaria de achar?\n>>'))
        # ax, termo q usuário gostaria de achar
        ax = a1 + r*(n-1)
        # formula para calculo de p.a
        print(f'\na{n} = {ax}\nDados: a1 = {a1}, r = {r}')
        # exibe os resultados
    elif prompt == '2':
        # condicional para terminação do programa
        print('\nFIM')
        # exibe mensagem
        exit()
        # termina o programa com código 0
    else:
        print('\nPor escolha uma das duas opções.')
        # caso o usuario entre uma opção errada, exibe uma mensagem

