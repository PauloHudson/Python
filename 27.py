
#ler numero até ser diferente de 0, quando for 0 ele para.


x=0
acumulador = 0
while True:
    nmr = int(input('Digite numeros inteiros: '))
    if(nmr == 0):
        print('------FINISH-------')
        break
    else:
        acumulador = acumulador + nmr
        x += 1

print(f' foram digitados {x} numeros, média {acumulador/x}')