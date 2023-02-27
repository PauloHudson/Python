#escreva um progrma que pergunte o deposito inicial e a taxa de juros de uma poupança. exiba os valores mesa mes para os 24 primeiros meses.
#escreva o total ganho com juros no periodo
DInicial = int(input('Digite o Deposito Inicial: '))
Tjuros = float(input('Digite a taxa de juros %: '))
ValorMes = int(input('Digite o valor Mensal de investimento'))
TjurosConvertida = Tjuros / 100
x = 1
acumulador = DInicial
while(x < 25):
    acumulador = acumulador + (acumulador * TjurosConvertida ) + ValorMes
    print(f'{x} mês = {acumulador:5.2f}')
    x += 1
 