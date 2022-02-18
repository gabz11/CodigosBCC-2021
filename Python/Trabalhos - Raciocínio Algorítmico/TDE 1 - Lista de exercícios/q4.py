# q4. cálculo IMC
print('Questão 4\n')
while True:
    # laço para sempre executar o programa até q o usuário digite comando p/sair
    print('\nCálculo IMC\n1. Calcular\n2. Sair')
    # mostra opções do programa
    prompt = input('\nEscolha uma opção\n>> ')
    # escolha de operação
    if prompt == '1':
        # condicional para operação principal
        peso = float(input('Qual é o seu peso? (KG)\n>>'))
        # pede o peso do usuário em kg
        altura = float(input('Qual é sua altura? (Em metros)\n>>'))
        # pede a altura do usuario em m
        imc = peso/(altura**2)
        # calculo do imc, a formula é peso/(altura)^2
        if imc < 17:
            # se imc < 17 exibir tal
            print(f'Seu IMC = {imc:.2f}(kg/m^2)\n Sua situação é: Muito abaixo do peso.')
        elif imc < 18.5:
            # se imc entre >= 17 e < 18.5 exibir tal
            print(f'Seu IMC = {imc:.2f}(kg/m^2)\n Sua situação é: Abaixo do peso.')
        elif imc < 25:
            # >= 18.5 e < 25 exibir tal
            print(f'Seu IMC = {imc:.2f}(kg/m^2)\n Sua situação é: Peso normal. ')
        elif imc < 30:
            # se imc >= 25 e < 30 exibir tal
            print(f'Seu IMC = {imc:.2f}(kg/m^2)\n Sua situação é: Acima do peso.')
        elif imc < 35:
            # se imc >= 30 e imc < 35 exibir tal
            print(f'Seu IMC = {imc:.2f}(kg/m^2)\n Sua situação é: Obesidade I.')
        elif imc < 40:
            # se imc >= 35 e imc < 40 exibir tal
            print(f'Seu IMC = {imc:.2f}(kg/m^2)\n Sua situação é: Obesidade II(Severa).')
        elif imc >= 40:
            # se imc >= 40 exibir tal
            print(f'Seu IMC = {imc:.2f}(kg/m^2)\n Sua situação é: Obesidade III(Mórbida).')
    elif prompt =='2':
        # condicional para saida do programa
        # exibe mensagem e finaliza com codigo 0
        print('\nFIM')
        exit()
    else:
        print('Por favor escolha uma das opções.')
        # caso o usuario coloque uma opção invalida, exibe texto