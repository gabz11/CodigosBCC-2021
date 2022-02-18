# Gabriel Farias | ex 7 lista 2 | check soma

# função recebe 2 numeros reais
def somase(a, b):
    # se a + b menor ou igual 20, subtrai-se 5 do montante
    if a + b <= 20:
        # retorna soma - 5
        return a + b - 5
    # caso for maior q 20 soma-se 8
    else:
        # retorna soma + 8
        return a + b + 8


pergunta = 'Número aqui\n>> '
num1 = float(input(pergunta))
num2 = float(input(pergunta))
print(f'Resultado: {somase(num1,num2)}')
