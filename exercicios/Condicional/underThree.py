# Problema "menor_de_tres"
# Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
# números lidos. Em caso de empate, mostrar apenas uma vez.

x = int(input("Enter a number : "))
y = int(input("Enter a number : "))
z = int(input("Enter a number : "))

if (x < y and x < z):
    print(x," is minor")
elif (y < x and y < z):
    print(y," is minor")
elif(z < y and z < x):
    print(z, " is minor")
elif(z == y or z == x):
    print(z, " is minor")
else :
    print(x, " is minor")