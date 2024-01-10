# Problema "glicose"
# Fazer um programa para ler a quantidade de glicose
# no sangue de uma pessoa e depois mostrar na tela a
# classificação desta glicose de acordo com a tabela de
# referência ao lado.

glucose = int(input("Enter the glucose nivel : "))

if(glucose <= 100 and glucose >= 0 ):
        print("Your glucose is normal")
elif(glucose > 100 and glucose < 140) :
        print("Your glucose is high")
elif(glucose > 140 and glucose > 0):
    print("Your have diabetes!")
else:
    print("The glucose cannot be less than 0")