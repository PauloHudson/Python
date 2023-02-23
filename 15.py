#receber dois numeros e vamos validar qual operação utilizar

def linha():
    print("---" * 10)



a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
linha()
print('/ for division, * multiplication, + sum and -ssubtraction ')
linha()
operation = input('enter the wished operation: ')
if(operation == "/"):
    print(a / b)
elif(operation == "*"):
    print(a * b)
elif(operation == "+"):
    print(a+b)
elif(operation == "-"):
    print(a-b)
else:
    print("Type only one of the options")
    print('/ for division, * multiplication, + sum and - subtraction')