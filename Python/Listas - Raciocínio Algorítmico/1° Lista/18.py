def salario():
    horaaula = float(input('Qual o valor pago por hora de aula?\n>> '))
    dias = int(input('Quantos dias de aula no mês?\n>> '))
    porcentagem = int(input('Qual a porcentagem descontada do INSS?'))
    montante = horaaula*dias
    liquido = montante - (montante*(porcentagem/100))
    return print(f'O salário liquido é {liquido}R$')


salario()