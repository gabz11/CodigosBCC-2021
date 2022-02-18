# q2 ler um numero e ver se ele é igual à
# 5,200,400 ou esta entre 500 e 1000
# ou fora destes escopos
num = int(input('Entre um número\n>> '))
# le o numero
if num == 5:
    # condicionais
    print('O número é igual à 5')
elif num == 200:
    print('O número é igual à 200')
elif num == 400:
    print('O número é igual a 400')
elif 500 <= num <= 1000:
    print(f'O valor está no intervalo de 500 à 1000\n500<={num}<=1000')
else:
    # num > 1000 or num < 500 entre parenteses pois somente uma sera verdade
    print('Não está nos escopos')