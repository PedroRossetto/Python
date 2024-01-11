# Problema "fatorial" (adaptado de URI 1153)
# Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
# fatorial de N.

x = int(input("Enter a number : "))
y = 0

if(x == 0):
    x+=1
k= x 
   
for j in range(x):
    y+=1

for i in range(x):
    y-=1
    if(y != 0):
        k=k*y
        
else:
    print(k)     
   