# def cria uma rotina
def adicao():
    # mensagem para ser exibida durante o prompt de input dos números
    prompt = 'Coloque um número \n>> '
    # entrada 1ro numero
    n1 = int(input(prompt))
    # entrada 2do numero
    n2 = int(input(prompt))
    # compara a soma de n1 + n2 para o caso que seja maior q 10
    if n1 + n2 > 10:
        #imprime a soma de n1 + n2
        print(n1+n2)
    # caso não seja verdade, faz isso
    else:
        # exibe ''null
        print('Null')


# chama a função adição
adicao()
#A procedure is a routine that can accept arguments
# but does not return any values. A function is a routine that can accept arguments and returns one or more values.