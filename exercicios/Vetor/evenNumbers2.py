# Problema "media_pares "
# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
# aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
# digitado, mostrar a mensagem "NENHUM NUMERO PAR"

n = int(input("Enter a number of numbers you want : "))

vector_n = [0 for x in range (n)]
qntEven = 0
totalEven = 0
qntOdd = 0

for i in range (n):
    vector_n[i] = int(input("Enter a number : "))
    if vector_n[i]%2==0 :
        qntEven+=1
        totalEven+=vector_n[i]
    if vector_n[i]%2!=0 :
        qntOdd+=1
        
if qntOdd==n :
    print("NO EVEN NUMBER !")        
else :
    avgEven = totalEven/qntEven
    print(f"Avarage sum of even numbers : {avgEven:.1f}")
