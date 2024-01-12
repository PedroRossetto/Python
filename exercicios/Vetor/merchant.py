# Problema "comerciante"
# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
# mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
# venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
# proporcionaram:
#  lucro < 10%
#  10% ≤ lucro ≤ 20%
#  lucro > 20%
# Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
# o lucro total.

profit = 0
item_name = []
sale_price = []
purchase_price = []
profit1 = 0
profit2 = 0
profit3 = 0
totalS = 0
totalP = 0

n = int(input("Enter the number of products you want to survey "))

for i in range (n):
    item_name.append(input("Enter the name of item : "))
    purchase_price.append(float(input("Enter the price of purchase item : ")))
    sale_price.append(float(input("Price of sale item : ")))
    
    if ((sale_price[i]-purchase_price[i])*100)/purchase_price[i] < 10 :
        profit1+=1
    elif ((sale_price[i]-purchase_price[i])*100)/purchase_price[i] >= 10 and ((sale_price[i]-purchase_price[i])*100)/purchase_price[i] < 20 :
        profit2+=1
    elif ((sale_price[i]-purchase_price[i])*100)/purchase_price[i] >= 20 :
        profit3+=1
    else:
        print("Error")
        
for j in range (n):
    totalS+= sale_price[j]
    totalP+= purchase_price[j]
   
profit = totalS-totalP       
print("REPORT : ")
print(" <= 10 : ", profit1)
print(" > 10 < 20 : ", profit2)
print(" > 20 : ", profit3)
print("price total purchase : $", totalP )
print("price total sale : $", totalS )
print("Total profit : $", profit)