# Problema "lanchonete" (adaptado de URI 1038)
# Uma lanchonete possui vários produtos. Cada produto possui um código
# e um preço. Você deve fazer um programa para ler o código e a
# quantidade comprada de um produto (suponha um código válido), e daí
# informar qual o valor a ser pago, com duas casas decimais, conforme
# tabela de produtos ao lado.

cod1 = 5
cod2 = 3.50
cod3 = 4.80
cod4 = 8.90
cod5 = 7.32

code = int(input("Enter the product code : "))
quantity = int(input("Enter the quantity of products that you purchased : "))

if code == 1 :
    total = cod1*quantity
    print(f"Total : ${total:.2f}")
elif code == 2 :
    total = cod2*quantity
    print(f"Total : ${total:.2f}")
elif code == 3 :
    total = cod3*quantity
    print(f"Total : ${total:.2f}")
elif code == 4 :
    total = cod4*quantity
    print(f"Total : ${total:.2f}")
elif code == 5 :
    total = cod5*quantity
    print(f"Total : ${total:.2f}")
else : 
    print("Product not exist !")