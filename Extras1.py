valor = int(input("Digite a quantidade de números que serão digitados: "))

x = 1
maior = -9999999999
while x <= valor:
    varx = int(input(f'Numero {x}: '))
    x += 1 
    if(varx > maior):
       maior = varx
print(f'Maior número digitado: {maior}')

