# Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
# combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
# médio do carro, com três casas decimais.

distance = int(input("Enter the distance traveled : "))
spentFuel = int(input("Enter the spent fuel : "))

avarageConsumption = distance/spentFuel


print(f"After traveling {distance} km and using {spentFuel} liters you consumed an average of {avarageConsumption:.3f} liters per km")