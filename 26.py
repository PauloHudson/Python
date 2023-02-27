#escreva um programa que pergunte o valor inicial de uma dívida, e o juros mensal, pergunte tamb´me
#o valor mensal que será pago, imprima o numero de meses para que a dívida seja paga, o total pago e o total de juros pago.
ValorInicial = int(input('Digite o valor inicial da dívida: '))
JurosMensal = int(input('Digite a quantidade de Juros: '))
ValorMensalSerPago = int(input("Valor Mensal a ser pago: "))


x = 0
conversor = ValorInicial/ValorMensalSerPago
total = ValorInicial
while(x < conversor):
          #inicial       +           #juros                * meses
    total = ValorInicial + (ValorInicial * JurosMensal/100) * conversor


    x += 1
print(f'A dívisa será paga em {x} vezes')
print(f'Dívida total de {total}')
print(f'Juros total de {total - ValorInicial}')