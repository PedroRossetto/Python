# Problema "operadora"
# Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
# telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
# ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.

quantityMinutes = int(input("Enter a quantity of minutes you used : "))
pricePlane = 50.00
additional = 2.00
total = float

if(quantityMinutes > 100):
    total = pricePlane+((quantityMinutes-100)*additional)
    print(f"Total to be paid: {total:.2f}")
elif(quantityMinutes < 0):
    print(f"Negative minutes")
else:
    print(f"total to be paid: {pricePlane:.2f}")