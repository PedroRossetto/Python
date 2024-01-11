# Problema "divisao" (adaptado de URI 1116)
# Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
# segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.

x = int(input("How many calculations do you want to type? : "))

for i in range (x):
    divisor = int(input("Enter the divisor : "))
    denominator = int(input("Enter the denominator : "))
    if(denominator == 0) :
        print("DIVISION IMPOSSIBLE")
    else :
        division = divisor/denominator
        print(f"DIVISION : {division:.2f} ")
        