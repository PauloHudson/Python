contador = 0
while True:
    valor = int(input(": "))
    if(valor == 0):
        break
    else:
        contador += valor
print(f"Resultado: {contador}")