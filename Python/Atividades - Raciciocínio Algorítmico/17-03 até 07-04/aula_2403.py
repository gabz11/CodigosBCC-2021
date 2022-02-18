# calculo de area, perimetro e diametro do circulo
raio = float(input('Qual o valor do raio?\n>> '))
pi = 3.14
# OBS valor de pi aproximado por questão do exercicio
diametro = 2*raio
perimetro = diametro*pi
area = raio**2*pi
print(f'Diametro:{diametro}\nPerimetro:{perimetro}\nÁrea:{area}')