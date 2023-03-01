#Leia um numero é diga se ele é primo ou não. calcuamos o resto da divisão do numero por 2 e depois or todos os numeros impares ateo o numero lido.
#2 é o único nuero primo que é par.





while True:
    v = 1
    x = (v % 3 != 0)
    v = int(input('Digite um Número (0 para parar): '))
    if(v == 0):
        break
    elif(v == 2):
        print('primo')
    elif(v % 2 != 0):
        if(v != x):
            print('primo')
    else:
        print('Não Primo')