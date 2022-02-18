# Questão 6
print('Questão 6')
print('Ordenar valores A,B e C de forma ascendente (Menor para o maior)')
# mensagem sobre operação
a = float(input('\nEntre o valor de A\n>>'))
b = float(input('\nEntre o valor de B\n>>'))
c = float(input('\nEntre o valor de C\n>>'))
# condiconais comparam os possiveis casos
# q são 6 no total
if a < b < c:
    print(f'A({a})<B({b})<C({c})')
elif a < c < b:
    print(f'A({a})<C({c})<B({b})')
elif b < a < c:
    print(f'B({b})<A({a})<C({c})')
elif b < c < a:
    print(f'B({b})<C({c})<A({a})')
elif c < a < b:
    print(f'C({c})<A({a})<B({b})')
elif c < b < a:
    print(f'C({c})<B({b})<A({a})')
