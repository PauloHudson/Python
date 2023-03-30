entrada = int(input("Digite o número dejesado: "))

contador = 0 
for c in range(2, entrada):
    if(entrada % c == 0):
        contador += 1
if(contador == 0):
    print("Numero primo")
else:
    print("Número não primo")
