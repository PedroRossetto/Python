# Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
# com quatro casas decimais):
# a) a área do quadrado que tem lado A
# b) a área do triângulo retângulo que base A e altura B
# c) a área do trapézio que tem bases A e B, e altura C

a = float(input("Enter the value of 'A' : "))
b = float(input("Enter the value of 'B' : "))
c = float(input("Enter the value of 'C' : "))

areaSquare = a*a
areaTriangle = (a*b)/2
areaTrapeze = (a+b)*c/2

print(f"The area of square is : {areaSquare:.4f}")
print(f"The area of triangle is : {areaTriangle:.4f}")
print(f"The area of trapeze is : {areaTrapeze:.4f}")
