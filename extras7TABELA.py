import math 
minimo = int(input("Digite o valor mínimo em graus C: "))
max =    int(input("Digite o valor máximo em Graus C: "))

c = minimo
def conversao(minimo, max):
    for c in range(minimo, max+5, 5):
        # print("temperatura em C")
        conversaoF =  math.floor((c * 1.8 ) + 32)
        print(f"{c:>18} {conversaoF:>18}")

    

print("  Temperatura em C   Temperatura em F")
conversao(minimo,max)

