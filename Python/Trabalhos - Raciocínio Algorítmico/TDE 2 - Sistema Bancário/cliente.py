import pickle
pickle_entrada = open("dados.pickle", "rb")
contas = pickle.load(pickle_entrada)
#print(contas)
# tirar do comentario para debug
def saida():
    pickle_saida = open("dados.pickle", "wb")
    pickle.dump(contas, pickle_saida)
    pickle_saida.close()
    exit()
def logar():
    # PROCESSO LOGIN
    tentativa = True
    con = 3
    while tentativa:
        numero_conta = input('\nDigite o n° da sua conta ou S para Sair.\n>> ')
        numero_conta.strip()
        if numero_conta.isnumeric() and " " not in numero_conta:
            numero_conta = int(numero_conta)
            if numero_conta in contas:
                login_senha = True
                while login_senha:
                    senha = input('\nDigite sua senha\n>> ')
                    if senha == contas[numero_conta]['senha'] and contas[numero_conta]['bloqueio'] == False and con > 0:
                        print('\nLogin concluido!')
                        return numero_conta
                        login_senha = False
                        tentativa = False
                    elif contas[numero_conta]['bloqueio'] == True:
                        print('Sua conta foi bloqueada por atividade SUSpeita, por favor contate o banco.\n')
                        login_senha = False
                    else:
                        con -= 1
                        if con > 0:
                            print(f'\nSenha inválida (Você tem {con} tentativas)')
                            tentar_novamente = True
                            while tentar_novamente:
                                tentar = input('\nTentar novamente?\n(S - Sim; N - Não)\n>> ')
                                if tentar == 'S' or tentar == 's':
                                    tentar_novamente = False
                                elif tentar == 'N' or tentar == 'n':
                                    tentar_novamente = False
                                    login_senha = False
                                else:
                                    print('\nErro: Opção inválida')
                        elif con <= 0:
                            print('Sua conta foi bloqueada\nEncerrando sua sessão.')
                            contas[numero_conta]['bloqueio'] = True
                            saida()
            else:
              print('Erro: n° da conta inválido.')  
        elif numero_conta == 'S' or numero_conta == 's':
            saida()
def acesso(numero_conta):
    # OPERAÇÕES
    def saldo(numero_conta):
        print(f"\nSeu saldo atual é {contas[numero_conta]['saldo']}R$.")
    def saque(numero_conta):
        # Saque
        if contas[numero_conta]['saldo'] <= 0:
            print('\nErro: Não há saldo.')
        else:
            q_saque = input('\nDigite o valor do saque\n>> ')
            if q_saque.isnumeric():
                q_saque = int(q_saque)
                if 0 < q_saque <= contas[numero_conta]['saldo']:
                    confirmacao = True
                    while confirmacao:
                        print(f'\nConfirmar saque de {q_saque}R$?')
                        prompt = input('(S - Sim |N - Não)\n>>')
                        if prompt == 'S' or prompt == 's':
                            contas[numero_conta]['saldo'] -= q_saque
                            print(f"\nSeu saldo agora é {contas[numero_conta]['saldo']}")
                            confirmacao = False
                        elif prompt == 'N' or prompt == 'n':
                            confirmacao = False
                        else:
                            print('\nErro:Opção inválida.')
                else:
                    print('Erro: Quantia invalida')
            else:
                print('Erro: Caractere detectado')
    def deposito(numero_conta):
        # Deposito
        q_deposito = input('\nDigite o valor do deposito\n>> ')
        if q_deposito.isnumeric():
            q_deposito = int(q_deposito)
            if 0 < q_deposito <= 10000:
                confirmacao = True
                while confirmacao:
                    print(f'\nConfirmar o deposito de {q_deposito}R$?')
                    prompt = input('\n(S - Sim | N - Não)\n>>')
                    if prompt == 'S' or prompt == 's':
                        contas[numero_conta]['saldo'] += q_deposito
                        print(f"Seu saldo atual é {contas[numero_conta]['saldo']}R$")
                        confirmacao = False
                    elif prompt == 'N' or prompt == 'n':
                        confirmacao = False
                    else:
                        print('\nErro: Opção inválida.')
            else:
                print('\nErro: Valor inválido')
        else:
            print('\nErro: Caractere detectado')
    def simular():
        print('Simulação de investimento (Tecle S para cancelar.)')
        operacao = True
        while operacao:
            numero_meses = input('Tempo em meses\n>> ')
            if numero_meses.isnumeric():
                numero_meses = int(numero_meses)
                operacao_2 = True
                while operacao_2:
                    aporte_inicial = input('Valor do aporte\n>>')
                    if aporte_inicial.isnumeric():
                        aporte_inicial = float(aporte_inicial)
                        taxa_rendimento = 0.015
                        if numero_meses < 60:
                            taxa_administracao = 0.01
                            montante = aporte_inicial*(1+taxa_rendimento)**numero_meses
                            print(f'Seu montante BRUTO é {montante:.2f}R$\n')
                            porcentagem_banco = montante*taxa_administracao
                            montante = montante - porcentagem_banco
                            print(f'Aplicando a taxa de adm. de {taxa_administracao*100}% totalizando '
                                  f'{porcentagem_banco:.2f}R$')
                            print(f'Seu montante liquido é {montante:.2f}R$')
                            operacao_2 = False
                            operacao = False
                        else:
                            taxa_administracao = 0.005
                            montante = aporte_inicial * (1 + taxa_rendimento) ** numero_meses
                            print(f'Seu montante BRUTO é {montante:.2f}R$\n')
                            porcentagem_banco = montante * taxa_administracao
                            montante = montante - porcentagem_banco
                            print(f'Aplicando a taxa de adm. de {taxa_administracao*100}% totalizando '
                                  f'{porcentagem_banco:.2f}R$')
                            print(f'Seu montante liquido é {montante:.2f}R$')
                            operacao_2 = False
                            operacao = False
                    elif aporte_inicial == 'S' or aporte_inicial == 's':
                        operacao_2 = False
                        operacao = False
                    else:
                        print('Erro: Valor/Opção inválida\n')
            elif numero_meses == 'S' or numero_meses == 's':
                operacao = False
            else:
                print('Erro: Valor/Opção inválida\n')
    print(f"\nBom dia Sr(a) {contas[numero_conta]['nome'].title()}!")
    logado = True
    while logado:
        print('\nSelecione a opção desejada.')
        print('\n1. Ver Saldo | 2. Saque | 3. Deposito | 4. Simular investimento | 5. Sair')
        prompt = input('\n>> ')
        if prompt == '1':
            saldo(numero_conta)
        elif prompt == '2':
            saque(numero_conta)
        elif prompt == '3':
            deposito(numero_conta)
        elif prompt == '4':
            simular()
        elif prompt == '5':
            print('Deslogando...')
            logado = False
        else:
            print('\nErro: Opção invalida.')
print('Bem-vindo ao banco A.M.O.G.U.S ඞ')
print('################################')
while True:
    numero_conta = logar()
    acesso(numero_conta)



