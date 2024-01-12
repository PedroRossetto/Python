# Problema "alturas"
# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
# bem como os nomes dessas pessoas caso houver.

n = int(input("Enter a amount of number you want : "))

name_vector = [0 for x in range (n)]
idade_vector = [0 for x in range (n)]
altura_vector = [0 for x in range (n)]
total_altura = 0
media = 0
porcent = 0
lessof16 = 0

for i in range (0, n):
    print("Enter the data of the  ", i+1,"º person")
    name_vector[i] = input("Name : ")
    idade_vector[i] = int(input("Years : "))
    altura_vector[i] = float(input("Width : "))
    

for j in range(n):
    total_altura += altura_vector[j]
    media = total_altura/n
    if(idade_vector[j] < 16):
        lessof16+=1
porcent = (lessof16*100)/n

print("The average height is : ", media)
print("The porcentage of people less 16 years is : ", porcent,"%")
for k in range(n):    
    
    if(idade_vector[k] < 16):
        print(name_vector[k])
