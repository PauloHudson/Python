#vair receber um valor
minutos = int(input('Digite quantos minutos fora usados: '))

if(minutos < 200):
    preco = 0.15
elif (minutos < 400):
    preco = 0.12
else:
    preco = 0.10
    
print(f'o valor a ser pago será de {minutos * preco}')
