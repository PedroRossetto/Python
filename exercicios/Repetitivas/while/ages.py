# Problema "media_idades"
# Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
# indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
# e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
# mostrar a mensagem "IMPOSSIVEL CALCULAR".

x = 0
total = 0
i = 0
x = int(input("Enter a number : "))
if x >= 0 : 
    i = 1 + i
    total = total + x
    while x >= 0 :
        x = int(input("Enter a number : "))
        i = 1 + i
        total = total + x
        if x < 0 : 
            media = total/i
            print("Media is : ", media)
else:
    print(x , "IS IMPOSSIBLE TO CALCULATE")
        

