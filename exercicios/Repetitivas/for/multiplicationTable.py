# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo.

x = int(input("Enter a number : "))

for i in range(10):
    i = 1 + i
    print(x*i)
 