# Problema "sequencia_impares" (adaptado de URI 1067)
# Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
# se for o caso.

x = int(input("Enter a number : "))

for i in range (x-1):
    i += 1
    print(i)