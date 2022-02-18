n1 = float(input('Digite a 1° nota\n>> '))
n2 = float(input('Digite a 2° nota\n>> '))
n3 = float(input('Digite a 3° nota\n>> '))
n4 = float(input('Digite a 4° nota\n>> '))
# ^^^ leitura das medias
media = (n1+n2+n3+n4)/4
# var atribuida pra soma das medias e divisão
if media < 4:
    # print(f para formatação
    print(f'\nMedia: {media}\n\tREPROVADO')
elif 4 <= media < 7:
    print(f'\nMédia: {media}\n\tRECUPERAÇÃO')
else:
    print(f'\nMédia: {media}\n\tAPROVADO')
# ^^^ condicionaios para os 3 possiveis casos