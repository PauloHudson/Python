#redução de vida de um fumante
#quantos cigarros vc fuma ao dia
#quantos anos vc fuma?
#perde 10min de vida a cada cigarro
#quantos dias ele perdera
import math


Cigarros = int(input('Quantos cigarros você fuma ao dia: '))
Anos = int(input('A Quantos Anos você fuma? '))
Valor = float(input('Qual o valor do maço (dia) ? '))
TotalCigarrosMes = (Cigarros * 30) 
TotalCigarrosAno = (TotalCigarrosMes * 12) 
GastoTotal = (((Cigarros / 20) * Valor) * 365) * Anos
# # horas
PercadaVida = Anos * 365 * Cigarros * 10 
dias = PercadaVida / (24 * 60)
print('----' * 10)
print(f'Você Fumou no mês {TotalCigarrosMes} Cigarros, no Ano {TotalCigarrosAno} cigarros, e gastou um total de R${GastoTotal:5.2f}')
print('----' * 10)
print(f'E perdeu {math.floor(PercadaVida)} Minutos de vida, ou {math.floor(dias)} dias de vida.')
print('----' * 10)



 