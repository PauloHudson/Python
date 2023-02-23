
import math


Valorcasa = int(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Quantos ano a pagar:')) * 12
print('-'*40)

prestacao = (math.floor(Valorcasa / anos))
porcentagem = (salario * 0.3)

if(prestacao > porcentagem):
    print('infelizmente você não poderá comprar, a prestação é acima de 30% do seu salário: ')
    print(f'Salário: R${salario}, 30% do salário = {porcentagem}, prestação = R${prestacao} ')
else:
    print('parabéns crédito liberado: ')
    print(f'Salário: R${salario}, 30% do salário = {porcentagem}, prestação = R${prestacao} ')