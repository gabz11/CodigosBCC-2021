# q3 - condicionais com leitura de 2 números
print('Questão 3.')
while True:
    # laço while para poder executar sempre o programa até o usuário o termine
    print('\nSoma de 2 números com condicionais.\n1. Calcular\n2. Sair')
    # mensagem das possiveis operações
    prompt = input('\nDigite uma opção\n>> ')
    # entrada para operação
    if prompt == '1':
        n1 = float(input('Entre o primeiro número\n>> '))
        # entrada do primeiro número
        n2 = float(input('Entre o segundo número\n>> '))
        # entrada do segundo número
        soma = n1 + n2
        # soma n1 + n2
        if soma <= 20:
            # condicional se a soma for menor ou igual à 20
            print(f'\nSoma = {soma}\nComo {soma}<= 20 o resultado é subtraido -5 então: {soma} - 5 = {soma-5}')
            # exibe a mensagem e faz o cálculo devido
            # nesse caso como se faz a regra, se o numero é 20 ou menor, operação fica soma - 5
        else:
            # condicional se a soma for maior que 20
            print(f'\nSoma = {soma}\nComo {soma}> 20 o resultado é somado +8 então: {soma} + 8 = {soma + 8}')
            # exibe a mensage e o calculo
            # como é maior q 20, a operação fica soma + 8
    elif prompt =='2':
        # condicional para sair do programa
        print('FIM')
        # exibe mensagem
        exit()
        # encerra o programa com código 0
    else:
        print('Por favor digite uma opção correta.')
        # exibe mensagem caso entrada do prompt n for válida