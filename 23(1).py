#escreva um programa que leia dois numeros. imprima a divisao inteira do primeiro pelo segundo, assim como o resto da divisão, utilize apenas os operadores
#de soma e subtracao para calcular o resultado, lembres-se de que podemos entender o quoficiente da divisão de dois números como a quantidade de vezes
#que podemos retirar o divisor do dividendo, logo 20 / 4 = 5, uma vez podemos subtriar 4 5 vezes de 20.

v1 = int(input('Digite o 1 valor: '))
v2 = int(input('Digite o 2 valor: '))
coeficiente = 0

Mutador = v1
while(Mutador >= v2):
    Mutador = Mutador - v2
    # x é igual a 4, pois é a quantidade de x que repetimos a subtração, que tiramos (4 vezes 5 de 20.)
    coeficiente += 1
resto = Mutador


print(f'{v1} / {v2} = {coeficiente}, resto {resto}')