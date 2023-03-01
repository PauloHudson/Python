lista = [0,0,0,0,0]
x =0
while x < 5:
    lista[x] = int(input('Coloque Dentro da lista...: '))
    x+= 1

while True:
    escolha = int(input('Escolha o índice a ser acessado (0 para parar): '))
    if escolha == 0:
        print('Operação encerrada')
        break
    print(f'Indíce Escolhido: {lista[escolha - 1]}')