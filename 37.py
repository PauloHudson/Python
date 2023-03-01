lista = []
while True: 
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    lista.append(valor)
x = 0
while x < len(lista):
    print(f'{x + 1}: {lista[x]}')
    x += 1