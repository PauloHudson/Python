#escreva um programa para controlar uma pequena máquina registradora. solicitar ao usuário que digite o códigoo do produtos. utilize a tabela de codigos a seguir para obter p reço de cada produto.



def tabela():
    print(f'-------------------')
    print('|  1   |   R$ 1.2  |')
    print('|  2   |   R$ 1.0  |')
    print('|  3   |   R$ 4.0  |')
    print('|  5   |   R$ 7.0  |')
    print('|  9   |   R$ 9.0  |')
    print(f'-------------------')
    
    

valorFinal = 0
produtos = 0
tabela()
while True:
    receber = int(input('Digite o Código do Produto (Apenas os Acima): '))
    if(receber == 0):
        print('encerrado')
        break
    elif(receber == 1):
        valorFinal = valorFinal + 0.5
        produtos += 1
    elif(receber == 2):
        valorFinal = valorFinal + 1
        produtos += 1
    elif(receber == 3):
        valorFinal = valorFinal + 4
        produtos += 1
    elif(receber == 5):
        valorFinal = valorFinal + 7 
        produtos += 1
    elif(receber == 9):
        valorFinal = valorFinal + 9
        produtos += 1
    else:
        tabela()
        print('código inválidos')

print(f'Você gastou R${valorFinal:5.2f} e comprou um total de {produtos} produtos')
    