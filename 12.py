#> de 1250 aumento de 10%
#< 1250 aumento de 15%
salario = int(input('Digite seu salario: '))
if(salario >= 1250):
    novo = ((salario * 0.10) + salario)
    print(f'Salário ajustado para {novo}')
else:
    new = ((salario * 0.15) + salario)
    print(f'Salário ajustado para {new}')