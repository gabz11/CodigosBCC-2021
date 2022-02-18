# q2. formula de heron
print('Questão 2.\n\n')
while True:
    # laço para sempre executar até q o usuário encerre o programa com uma opção
    print('\nCálculo da área de um triângulo(Formula de Heron)\n1. Calcular\n2. Sair')
    prompt = input('Digite sua opção\n>> ')
    if prompt =='1':
        # condicional para calculo
        a = float(input('Digite o valor do lado a\n>> '))
        # entrada lado a
        b = float(input('Digite o valor do lado b\n>> '))
        # entrada lado b
        c = float(input('Digite o valor do lado c\n>> '))
        # entrada lado c
        p = (a+b+c)/2
        # calculo perimetro
        area = (p*(p-a)*(p-b)*(p-c))**(1/2)
        # formula área
        print(f'Resultado\nÁrea = {area} (unidades)\nPerimetro = {p}\nDados: a = {a}, b = {b}, c = {c}')
        # exibe os resultados
    elif prompt =='2':
        # condicional para saida
        print('FIM')
        # exibe mensagem
        exit()
        # termina o programa com código 0
    else:
        # se não for opção correta, exibir mensagem
        print('\nComando inválido...')

