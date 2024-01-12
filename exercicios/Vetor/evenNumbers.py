# Problema "numeros_pares"
# Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
# tela todos os números pares, e também a quantidade de números pares.

n = int(input("Enter a number of numbers you want : "))
vector1 = [0 for x in range (n)]
qnt = 0

for i in range (n):
    vector1[i] = int(input("Enter a number : "))

for j in range (n):
    if vector1[j]%2==0:
        qnt+=1
        print(vector1[j])
    
print("Quantity a even numbers :", qnt)