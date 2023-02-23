#programa ter 3 numeros falar qual o maior
nm1 = int(input('Digite um valor: '))
nm2 = int(input('Digite um valor: '))
nm3 = int(input('Digite um valor: '))

maior = 0
if(nm1 > maior):
    maior = nm1
    if(nm2 > maior):
        maior = nm2
        if(nm3 > maior):
            maior = nm3
print(f'maior numero {maior}')
        