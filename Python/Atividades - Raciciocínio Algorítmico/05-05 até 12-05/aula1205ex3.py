pratos = []
peso = input("Qual o peso do prato?(P para parar)\n>>")
while peso !='P':
    peso = float(peso)
    pratos.append(peso)
    peso = input("Qual o peso do prato?(P para parar)\n>>")
q_pratos = len(pratos)
contador_800 = 0
acum_pratos = 0
for i in range(len(pratos)):
    p = pratos[i]
    acum_pratos += p
    if p > 0.8:
        contador_800 += 1
media_pesos = acum_pratos/ q_pratos
print(f'Média de pesos: {media_pesos} ')
print(f'Qtd de pratos > de 800g: {contador_800}')