# Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
# da área, perímetro e diagonal deste retângulo, com quatro casas decimais
import math

width = float(input("Digite a altura do retangulo : "))
height = float(input("Digite a base do retangulo : "))

area = width*height
perimeter = (2*width)+(2*height)
diagonal2 = (width**2)+(height**2)
diagonal = math.sqrt(diagonal2)



print(f"O valor do perimetro é : {perimeter:.4f}")
print(f"O valor da area é : {area:.4f} ")
print(f"O valor da diagonal do retangulo é : {diagonal:.4f} ")
