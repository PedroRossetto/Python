#Crie um programa em Python que solicite ao usuário um número inteiro positivo e, em seguida, imprima uma contagem regressiva a partir desse número até 1. Por exemplo, se o usuário inserir o número 5, o programa deve imprimir 

num = int(input("Digite o valor que deseja"))


for n in range(num, 0, -1):
    print(num)
    print(n)
 
