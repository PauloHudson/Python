#escreva um programa que exiba um menu, adicao subtracao, divisao e multi. 
#imprima a tabuada do nmr desejado ate que a opcao de saida seja efetivada.
def printar():
    print("""

    Menu
    ----
    1 - Adição
    2 - Subtração
    3 - Divisão
    4 - Multiplicação
    0 - Sair

    """)
printar()
while True:
    escolha = int(input('Digita a opção desejada (caso deseje parar digite 0): '))
    if(escolha == 0):
        print('----'*20)
        print('Operação Parada!!!')
        print('----'*20)
        break
    elif escolha > 0 and escolha < 4:
        nmr = int(input('Digite a tabuada do numer0 a ser gerado: '))
        x= 1
        while x <= 10:
            if(escolha == 4):
                print(f'{nmr} / {x} = {nmr/x:5.2f}')
            elif(escolha == 1):
                print(f'{nmr} + {x} = {nmr+x:5.2f}')
            elif(escolha == 2):
                print(f'{nmr} - {x} = {nmr-x:5.2f}')
            elif(escolha == 3):
                print(f'{nmr} * {x} = {nmr*x:5.2f}')
            x = x + 1
    else:
        printar()
        print('Opção Inválida, escolha entre as opções acima')
