

soma = 0
contador = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    soma += valor
    contador += 1

print(f'a soma de tudo é {soma}, total de {contador} numeros, média de {soma/contador:.^5.2f}')