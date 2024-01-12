# Problema "maior_posicao"
# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
# o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
# considerando a primeira posição como 0 (zero).

n = int(input("Enter a number of numbers you want : "))
vector = [0 for x in range (n)]
position = 0
highness = 0

for i in range (n):
    vector[i] = int(input("Enter a number :"))
    if (vector[i] > highness):
        position = i
        highness = vector[i]
        
        
print("The position :", position)
print("THe highness number is :", highness)