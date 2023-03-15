#faça um progrma que percorra duas listas e gere uma terceira sem elementos repetidos.

# inserindo em A
listaA = []

while True:
    insertA = int(input('Digite o valor a ser inserido: '))
    listaA.append(insertA)
    if (insertA == 0):
        break
# inserido em B
ListaB = []

while True:
    insertB = int(input('Digite o valor a ser inserido na segunda lista: '))
    ListaB.append(insertB)
    if(insertB == 0):
        break
# -------------------------------------------
# lista all tem a e b
listaALL = listaA[:]
listaALL.extend(ListaB)
# -----
x = 0
ListaC = []
# ----------------
while x < len(listaALL):
    y = 0
    while y < len(ListaC):
        if listaALL[x] == ListaC[y]:
            break
        y += 1
        # vai dar um append nos vaores que nao sao iguais (repetidos)
    if y == len(ListaC):
        ListaC.append(listaALL[x])
    x += 1
x = 0
while x < len(ListaC):
    print(f"{x}: {ListaC[x]}")
    x = x + 1