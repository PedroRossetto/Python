# Problema "troco_verificado"
# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
# O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
# e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
# ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
# valor restante conforme exemplo.

priceU = float(input("Enter the price unity : "))
quantity = int(input("Enter the quantity of itens : "))
moneyReceived = float(input("Enter the money received : "))
total = priceU*quantity
change = moneyReceived-total

if (moneyReceived < total) :
    missing = total-moneyReceived
    print(f"Money is missing, {missing:.2f} dollars are missing")
else:
    print(f"The change is : {change:.2f}")