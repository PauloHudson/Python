#faça um prograa que calcule o tempo de uma viagem de carro, pergunte a distancia e a veocidade media  esperda pela viagem...
import math



distancia = int(input('qual a distância: '))
velocidade = int(input('qual a velocidade: '))
convensor = (math.floor(distancia))



print(f' {distancia} Km, em uma velocidade de {velocidade}, chegaremos em {math.floor(distancia/velocidade)}' )