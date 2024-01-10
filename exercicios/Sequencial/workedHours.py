# Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
# quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
# uma mensagem explicativa, conforme exemplo.

name = input("Enter your name : ")
priceHour = float(input("Enter the price for your hours worked : "))
hoursWorked = float(input("Enter your hours worked : "))

salary = priceHour*hoursWorked

print(f"{name}, your salary is : ${salary:.2f}")