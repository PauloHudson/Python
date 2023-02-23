# faça um programa que calcule o aumento de um salario, ele é dado o valor do salário e a porcentagem do aumentoo...

salario = int(input('qual o seu salário: '))
aumento = int(input('qual a % de aumento: '))
print(f'O seu salário era de R${salario:5.2f}, recebeu um aumento de {aumento}% e agora é R${((salario * aumento) /100) + salario:5.2f}')