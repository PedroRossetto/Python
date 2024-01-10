# Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
# O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
# e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
# mostrar o valor do troco a ser devolvido ao cliente.

priceU = float(input("Enter the price of itens : "))
quantity = int(input("Enter the quantity of itens : "))
moneyReceived = float(input("Enter the money received : "))

change = moneyReceived-(priceU*quantity)

print(f"CHANGE :  {change:.2f}")