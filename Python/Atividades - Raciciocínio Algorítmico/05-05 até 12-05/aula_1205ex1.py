anacleto = 1.50
felisberto = 1.10
tx_anacleto = 0.02
tx_felisberto = 0.03
ano = 0
while felisberto <= anacleto:
    anacleto += tx_anacleto
    felisberto += tx_felisberto
    ano += 1
    print(f'Ano: {ano}|Anacleto:{anacleto}|Felisberto:-{felisberto}')