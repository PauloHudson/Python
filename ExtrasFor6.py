from math import sqrt
while True:
    p0x = input("valor de X para p0: ")
    if(p0x == "sair"):
        break
    else:
        p0y = int(input("valor de Y para p0: "))
        p1x = int(input("valor de X para p1: "))
        p1y = int(input("valor de Y para p1: "))
        distancia = sqrt((int(p0x) - p1x)**2 + (p0y - p1y)**2)
        print(f"Distancia: {distancia}")