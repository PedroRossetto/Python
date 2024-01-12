# Problema "mais_velho"
# Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
# devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
# da pessoa mais velha.

n = int(input("Enter a number of people : "))
nome = [0 for x in range (n)]
idade = [0 for x in range (n)]
moreOlder = 0
ageOlder = 0

for i in range (n):
    print(i+1, "ª person data")
    nome[i] = input("Name :")
    idade[i] = int(input("Age : "))
    
    
for j in range (n):
    if idade[j] > ageOlder:
        moreOlder = nome[j]
        ageOlder = idade[j]
        
print("More older is :", moreOlder, "he/she is : ", ageOlder, "years old.")