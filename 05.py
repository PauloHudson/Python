#mercadoria e a porcentagem de desconto, exiba o valor da mercadoria e o total a pagar
def linha():
    print('----' * 2)




item = input('Digite o nome do Produto:')
linha()
mercadoria = int(input('Digite o Valor da mercadoria: '))
linha()
desconto = int(input('digite o valor de desconto: '))
print(f'Você comprou {item}, Preço normal R${mercadoria:5.2f}, recebeu um desconto de {desconto}%, preço final R${(((mercadoria * desconto) / 100) - mercadoria) * -1}')