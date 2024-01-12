# Problema "negativos"
# Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
# e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos.

n = int(input("Enter the amount of number you want : "))

Neg = [0 for x in range (n)]

if n<=10:
    for i in range (0, n):
        Neg[i] = int(input("Enter a number : "))
    
else:
    print("Enter a number less than 10")
    
for j in range (n):
    if Neg[j] < 0:
        print(Neg[j])