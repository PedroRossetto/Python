# Problema "crescente" (adaptado de URI 1113)
# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
# mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
# programa deve finalizar quando forem digitados dois valores iguais.

x = 0
y = 1

while x != y :
    x = int(input("Enter any number : "))
    y = int(input("Enter any more number : "))
    
    if(x < y) :
        print("Ascending order")
    else :
        print("Decending order")