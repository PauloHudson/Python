


km = int(input('Qual a velocidade(km/h): '))
if(km > 80):
    print(f'Você foi multado em R$ {((80 - km) * 5 )* -1}, {(km - 80)}Km Acima da velocidade permitida')
else:
    print('Dirija com cuidado!')