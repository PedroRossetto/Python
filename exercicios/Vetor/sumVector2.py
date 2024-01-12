# Problema "soma_vetores"
# Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
# terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
# o vetor C gerado.

n = int(input("Enter a number of numbers in you want in each vector : "))
vector_a = [0 for x in range (n)]
vector_b = [0 for x in range (n)]

for i in range (n):
    vector_a[i] = int(input("Enter a number for vector A : "))
    
for k in range (n):
    vector_b[k] = int(input("Enter a number for vector B : "))

print("Sum of vectors")    
for j in range (n):
    print(vector_a[j]+vector_b[j])