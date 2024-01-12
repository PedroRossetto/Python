# Problema "soma_vetor"
# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor

n = int(input("Enter a number amount of number you want : "))

vector = [0 for x in range (n)]
sum = 0

for i in range(0, n):
    vector[i] = int(input("Enter a number : "))
    

for j in range (n):
    sum+= vector[j] 
    
print("The sum of all numbers than vector is :", sum)
print("The media of all numbers than vector is", (sum/n))
 