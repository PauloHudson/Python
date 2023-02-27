#acumulador



n= 0
acumulador = 0
while(n != 0):
    numeros = int(input('Digite os Números: '))
    acumulador = acumulador + numeros
    n += 1
print(f'a soma desses {n} numeros é {acumulador}')
print(f'e a sua média aritmética é {acumulador/n}')