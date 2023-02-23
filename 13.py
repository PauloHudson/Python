preco = int(input('Digite o valor em KM: '))
if(preco <= 100):
    print(f'Você paragará R${preco * 0.5:5.2f}')
else:
    print(f'Você paragará R${preco * 0.45:5.2f}')   