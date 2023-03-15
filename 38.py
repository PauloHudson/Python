lista = []


while True:
    a = int(input('Digite um valor: '))
    lista.append(a)
    if a == 0:
        break
x = 0
while x < len(lista):
    print(f'{x+1} = {lista[x]}')
    x +=  1