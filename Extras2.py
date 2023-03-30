entrada = int(input("Digite o núero desejado: "))
e = 1
for c in range(1, entrada+1):

    e += 1/c 

print(f"{e:.3f}")
