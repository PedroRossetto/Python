# Problema "media_ponderada" (adaptado de URI 1079)
# Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
# teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
# que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
# que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
# pela soma dos pesos.

N = int(input("Enter a quantity of numbers : "))
total = 0
weighted = 0
numbers = []
for i in range (N):
    x = float(input("Enter a number : "))
    numbers.append(x)
    total +=1
total = total + 7   
numbers[0] *= 2
numbers[1] *= 3
numbers[2] *= 5
for number in numbers:
    weighted += number
    
weightedTotal = weighted/total
print(f"{weightedTotal:.2f}")


 