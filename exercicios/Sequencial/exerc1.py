# Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
# casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
# o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
# duas casas decimais, conforme exemplo.

width = int(input("Digite a largura : "))
length = int(input("Digite o comprimento : "))

priceM2 = float(input("Digite o valor do metro quadrado : "))

m2 = width*length

totalPrice = m2*priceM2

print(f"O preço do terreno é de : {totalPrice:.2f}")