notas = [0,0,0,0,0]
x = 0
soma = 0
while x < 5:
    notas[x] = float(input('Digite a Nota: '))
    soma += notas[x]
    x += 1
x = 0
for x in range(5):
    print(f'{x} nota: {notas[x]}')
    x +=1