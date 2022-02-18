# questão 8
print('Questão 8')
# questão sobre dosagem de um medicamento conforme idade e peso
while True:
    # sempre executar o programa até q o usuario até entrada do usuário para sair
    print('\nCalculo da dosagem de um medicamento\n1. Iniciar\n2. Sair')
    # mostra possiveis opções do prompt
    prompt = input('\nEscolha uma opção\n>> ')
    # entrada prompt
    if prompt == '1':
        # condicional principal para saida
        mg_por_gota = 25
        # Quantos mg por gota, como 500mg tem 1 ml e 1ml equivale à 20 gotas então 1 gota equivale à 25mg q equivale
        # à 0.25 ml, utilizado para calcular o número de gotas
        mg_ml_padrao = 500
        # 1 ml equivale 500mg, conveção utilizada para descobrir o ml equivalente por dosagem
        idade = int(input('\nQual a idade do paciente?\n>> '))
        # pede a idade do usuário
        if idade < 12:
            # condicional para pacientes com menos de 12 anos de idade
            peso = float(input('\nQual é o peso do paciente?(Em Kg)\n>> '))
            # entrada para o peso do usuário
            if peso < 9.1:
                # condicionais para verificar o peso e atribuir a dosagem de acordo com a tabela
                # providenciada pelo exercicio
                dose = 125
                print(f'A dosagem para crianças com o peso de {peso}Kg é {dose}mg')
                print(f'\nIsso equivale à {dose/mg_por_gota:.0f} gotas que equivalem {dose}mg({dose/mg_ml_padrao}ml)')
            # *** CASO ANTERIOR APLICA AOS PROXIMOS CONDICIONAIS
            elif peso < 16:
                dose = 250
                print(f'A dosagem para crianças com o peso de {peso}Kg é {dose}mg')
                print(f'\nIsso equivale à {dose/mg_por_gota:.0f} gotas que equivalem {dose}mg({dose/mg_ml_padrao}ml)')
            elif peso < 24:
                dose = 375
                print(f'A dosagem para crianças com o peso de {peso}Kg é {dose}mg')
                print(f'\nIsso equivale à {dose/mg_por_gota:.0f} gotas que equivalem {dose}mg({dose/mg_ml_padrao}ml)')
            elif peso <= 30:
                dose = 500
                print(f'A dosagem para crianças com o peso de {peso}Kg é {dose}mg')
                print(f'\nIsso equivale à {dose/mg_por_gota:.0f} gotas que equivalem {dose}mg({dose/mg_ml_padrao}ml)')
            elif peso > 30:
                dose = 750
                print(f'A dosagem para crianças com o peso de {peso}Kg é {dose}mg')
                print(f'\nIsso equivale à {dose/mg_por_gota:.0f} gotas que equivalem {dose}mg({dose/mg_ml_padrao}ml)')
        elif idade >= 12:
            # condicional se idade >= 12 anos
            peso = float(input('\nQual é o peso do paciente?(Em Kg)\n>> '))
            # pede peso do paciente
            if peso < 60:
                # condicionais para atribuir dosagem dependendo do peso
                dose = 875
                print(f'A dosagem pacientes acima de 12 anos com o peso de {peso}Kg é {dose}mg')
                print(f'\nIsso equivale à {dose/mg_por_gota:.0f} gotas que equivalem {dose}mg({dose/mg_ml_padrao}ml)')
            elif peso >= 60:
                dose = 1000
                print(f'A dosagem pacientes acima de 12 anos com o peso de {peso}Kg é {dose}mg')
                print(f'\nIsso equivale à {dose/mg_por_gota:.0f} gotas que equivalem {dose}mg({dose/mg_ml_padrao}ml)')
    elif prompt =='2':
        # condicional para terminar o programa
        print('FIM')
        # exibe mensagem de termino
        exit()
        # fecha o programa com código 0
    else:
        print('Por favor coloque uma opção válida')
        # exibe mensagem caso entrada do prompt seja invalida




