# Questão 5
print('Questão 5.')
while True:
    # laço p/executar o programa p/sempre até q o usuario opte por sair
    print('\nVerificar se um número é divisivel por 3 e 7 ao mesmo tempo\n1. Iniciar\n2. Sair')
    # exibe operações para entrada no prompt
    prompt = input('\nSelecione uma opção\n>>')
    # entrada da operação
    if prompt == '1':
        # condicional principal
        num = int(input('Entre um número\n>>'))
        # entrada do número
        if num % 3 == 0 and num % 7 == 0:
            # % verifica o resto, se resto 0, é divisivel, caso contrário ñ é
            # para satisfazer a condição tem q ser verdade para os 2 casos se for apenas
            # para 3 ou 7 é facil pois o exercicio pede para ser para os 2 casos.
            print(f'{num} é divisivel por 3 e 7 concomitantemente.')
            # mensagem dizendo q é divisivel
        else:
            print(f'{num} não é divisivel por 3 e 7 concomitante.')
            # mensagem dizendo q n é divisivel
    elif prompt == '2':
        # condicional para saida
        print('\nFIM')
        # mensagem
        quit()
        # encerra o programa com código 0
    else:
        print('\nPor favor, entre uma opção válida.')
        # exibe mensagem caso prompt receber dado n válido