import pickle
# importa pickle
pickle_a = open("dados.pickle", "rb")
contas = pickle.load(pickle_a)
# Tirar do comentario para printas as contas
# print(contas)
# Conta criada como exemplo de número 10005 já
def cadastro():
    # função
    # cadastrar conta
    # padrão conta
    conta = {'numero_conta': '', 'senha': '', 'saldo': 0, 'nome': '', 'profissao': '', 'renda_mensal': '',
             'endereco': '','telefone': '','bloqueio': False}
    # entrada de dados do cadastro
    nome = input('\nQual o nome completo do cliente?\n>> ')
    conta['nome'] = nome
    profissao = input('\nQual a profissão do cliente?\n>> ')
    conta['profissao'] = profissao
    renda_mensal = input('\nQual a renda mensal do cliente?\n>> ')
    conta['renda_mensal'] = renda_mensal
    endereco = input('\nQual o endereço do cliente?\n>> ')
    conta['endereco'] = endereco
    telefone = input('\nQual o n° de telefone do cliente?\n>> ')
    conta['telefone'] = telefone
    # booleano para processo do cadastro
    cadastro_conta = True
    while cadastro_conta:
        numero_conta = input('\nCrie um número para a conta\n>> ')
        if numero_conta.isnumeric():
            numero_conta = int(numero_conta)
            if 10000 <= numero_conta <= 99999:
                if numero_conta not in contas:
                    conta['numero_conta'] = numero_conta
                    cadastro_senha = True
                    while cadastro_senha:
                        senha = input('\nCrie uma senha\n>> ')
                        if 4 <= len(senha) <= 8 and senha.isalnum() and " " not in senha:
                            conta['senha'] = senha
                            contas.update({numero_conta: conta})
                            cadastro_senha = False
                            cadastro_conta = False
                        else:
                            print('\nErro: A senha deve ser alfanumérica, não conter espaços, e '
                                  'ter entre 4 á 8 caractéres.')
                else:
                    print('Erro: Já existe uma conta com esse número')
            else:
                print('Erro: a conta deve possuir 5 digitos (Ex: 10000)')
        else:
            print('Erro: Caracteres são inválidos')
def consulta():
    nome = input('\nQual o nome do cliente?\n>>')
    nome.strip()
    contador_contas = 0
    cliente_contas = []
    for conta in contas.values():
        if nome in conta.values():
            cliente_contas.append(conta)
            contador_contas += 1
    if contador_contas >= 1:
        print(f'\nHá {contador_contas} contas no nome de "{nome.title()}":\n')
        for conta in cliente_contas:
            print(f"Conta n° {conta['numero_conta']}")
    else:
        print(f'\nNão há contas no nome de "{nome.title()}"\n')
def nova_senha():
    numero_conta = input('Qual o número da conta?\n>> ')
    numero_conta.strip()
    if numero_conta.isnumeric():
      numero_conta = int(numero_conta)
      if numero_conta in contas:
          cadastro_senha = True
          while cadastro_senha:
              senha = input("\nCrie uma nova senha\n>> ")
              if 4 <= len(senha) <= 8 and senha.isalnum() and " " not in senha:
                  contas[numero_conta]['senha'] = senha
                  cadastro_senha = False
              else:
                  print('\nErro: A senha deve ser alfanumérica, não conter espaços, e ter entre 4 á 8 caractéres.')
      else:
          print('Essa conta não existe.')
    else:
      print('Erro: Valor inválido')
def desbloquear():
    print('Desbloqueio de conta.')
    numero_conta = input('Qual o número da conta?\n>> ')
    numero_conta.strip()
    if numero_conta.isnumeric():
        numero_conta = int(numero_conta)
        if numero_conta in contas:
            prompt = input('Digite "DESBLOQUEAR" para efetivar o desbloqueio\n>> ')
            prompt.strip()
            if prompt == 'DESBLOQUEAR' and contas[numero_conta]['bloqueio'] == True:
                print(f'A conta n° {numero_conta} foi desbloqueada.')
                contas[numero_conta]['bloqueio'] = False
            elif prompt == 'DESBLOQUEAR' and contas[numero_conta]['bloqueio'] == False:
                print(f'\nERRO: A conta não está bloqueada.')
            else:
                print('Operação cancelada')
        else:
            print('Conta não encontrada.')
    else:
        print('Erro: Valor inválido')
def remover():
    print('Fechar conta\n')
    numero_conta = input('Qual o número da conta?\n>> ')
    numero_conta.strip()
    if numero_conta.isnumeric():
        numero_conta = int(numero_conta)
        if numero_conta in contas:
            prompt = input('Digite "CONFIRMAR" para efetivar a exclusão da conta\n>>')
            if prompt == 'CONFIRMAR':
                del contas[numero_conta]
                print(f'A conta n° {numero_conta} foi terminada do sistema\n')
            else:
                print('Operação cancelada.')
        else:
            print('Conta não encontrada.\n')
    else:
        print('Erro: Valor inválido\n')
def saida():
    pickle_saida = open("dados.pickle", "wb")
    pickle.dump(contas, pickle_saida)
    pickle_saida.close()
    exit()
print('Olá gerente do banco A.M.O.G.U.S ඞ')
while True:
    print('\nSelecione uma opção:\n1. Cadastrar uma nova conta\n2. Buscar conta\n3. Definição de nova senha\n'
          '4. Desbloquear Conta\n5. Remover conta\n6. Sair')
    prompt = input('\n>> ')
    if prompt == '1':
        cadastro()
    if prompt == '2':
        consulta()
    if prompt == '3':
        nova_senha()
    if prompt == '4':
        desbloquear()
    if prompt == '5':
        remover()
    if prompt == '6':
        saida()

