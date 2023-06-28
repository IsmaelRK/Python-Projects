def soma(): 
    x = int(input("X:\t")) 
    y = int(input("Y:\t"))
    
    soma = x + y 

    print(soma)
    print("\n")

def sub():
    x = int(input("X:\t")) 
    y = int(input("Y:\t"))

    sub = x - y

    print(sub)
    print("\n")


def div():
    x = int(input("X:\t")) 
    y = int(input("Y:\t"))

    div = x / y

    print(div)
    print("\n")


def mult():
    x = int(input("X:\t")) 
    y = int(input("Y:\t"))

    mult = x * y

    print(div)
    print("\n")

op = 500

while op != 0:

    print("0 - Encerrar")
    print("1 - SOMA")
    print("2 - SUBTRACAO")
    print("3- DIVISAO")
    print("4 - MULTIPLICACAO")
    print("\n")

    op = int(input("\n"))

    if(op == 1):
        soma()

    if(op == 2):
        sub()

    if(op == 3):
        div()
    
    if(op == 4):
        mult()