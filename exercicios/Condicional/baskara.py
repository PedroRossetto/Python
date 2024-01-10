# Problema "baskara"
# Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
# de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
# conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.
import math

a = float(input("Enter the value of 'A' : "))
b = float(input("Enter the value of 'B' : "))
c = float(input("Enter the value of 'C' : "))

delta = b**2 - 4*a*c


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")
elif delta == 0:
    x = -b / (2*a)
    print(f"The equation has a single real root: {x:.4f}")
else:
    print("This equation does not have real roots.")


