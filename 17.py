QuantidadeKWh = int(input('Digite a quantidade KWh: '))


print('R para residencia, I para industria, C para comércio')
tipo = input('Digite o tipo de instalação: ').upper()

if(tipo == "R"):
    if(QuantidadeKWh <= 500):
        print(f'Você pagará R${QuantidadeKWh * 0.40}')
    else:
        print(f'Você pagará R${QuantidadeKWh * 0.65}')

elif(tipo == "I"):
    if(QuantidadeKWh <= 500):
        print(f'Você pagará R${QuantidadeKWh * 0.55}')
    else:
        print(f'Você pagará R${QuantidadeKWh * 0.60}')
        
elif(tipo == "C"):
    if(QuantidadeKWh <= 500):
         print(f'Você pagará R${QuantidadeKWh * 0.55}')
    else:
         print(f'Você pagará R${QuantidadeKWh * 0.59}')