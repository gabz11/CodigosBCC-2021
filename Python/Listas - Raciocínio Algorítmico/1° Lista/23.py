numero = 2019
n1 = numero % 10
n2 = (numero % 10) % 10
n3 = (numero % 100) % 10
n4 = (numero % 1000)
numerofinal = n1 * 1000 + n2 * 100 + n3 * 10 + n4 * 1
print(n1)
print(n2)
print(n3)
print(n4)
print(numerofinal)