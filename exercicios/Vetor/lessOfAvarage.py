# Problema "abaixo_da_media"
# Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
# mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
# os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.

n = int(input("Enter a number of numbers you want : "))
vector = [0 for x in range (n)]
total = 0
media = 0

for i in range(n):
    vector[i] = int(input("Enter a number : "))
    total += vector[i]
    
media = total/n

print("The avarage is : ", media)
print("Bellow avarage numbers : ")
for j in range(n):
    if vector[j]<media :
        print(f"{vector[j]:.1f}")