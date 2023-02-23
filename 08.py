# 1. quantidade de kms percrrids, por um carro alugado pel usuario, a quantidade de dias, 
#carro cuts 60 por dia 0.15 por km rodado
km = int(input('Quantos Km Foram rodados com o carro: '))
dias = int(input('Quantos dias o carro foi alugado: '))
print(f'O carro foi alugado por {dias} dias, total de  R${dias*60:5.2f}, percorreu um total de {km} Km, total R${km*0.15:5.2f}, total geral: R${(dias*60)+(km*0.15):5.2f}')