# Problema "aprovados"
# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
# no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
# os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
# igual a 6.0 (seis).

n = int(input("Enter a number of student : "))
name = [0 for x in range (n)]
a1 = [0 for x in range (n)]
a2 = [0 for x in range (n)]

aproved = []

for i in range(n):
    print("Data of ", i+1, "ª people")
    name[i] = input("Name :")
    a1[i]= float(input("1ª test score: "))
    a2[i]= float(input("2ª test score: "))
    
    if (a1[i]+a2[i])/2>6 :
       aproved.append(name[i])


        

print("Stundents approved : ")        
for aprov in aproved:
    print(aprov)