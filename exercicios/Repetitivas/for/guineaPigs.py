# Problema "experiencias" (adaptado de URI 1094)
# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
# organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
# quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
# laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
# informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
# utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
# valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
# inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
# de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
# cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
# percentual deve ser apresentado com dois dígitos após o ponto.
quantity = 0
type = 0
quantityRabbits = 0
quantityFrogs = 0
quantityMouses = 0
totalQuantity = 0 
percentRabbits = 0
percentFrogs = 0
percentMouses = 0

quantity = int(input("Enter the amount of test that will be entered : "))

for i in range (quantity):
    totalQuantity = int(input("Quantity of guinea pigs : "))
    if(totalQuantity < 1) :
        print("Number less than 1")
        break
    
    else :   
        type = input("Enter a type of guinea pig : ")
        if(type.lower() == "r"):
                quantityRabbits += totalQuantity
        elif(type.lower() == "f"):
                quantityFrogs += totalQuantity
        elif(type.lower() == "m"):
                quantityMouses += totalQuantity
        else:
                print("Type incorrect!")
                
totalQuantity = quantityFrogs+quantityMouses+quantityRabbits
percentRabbits = (totalQuantity*quantityRabbits)/100
percentFrogs = (totalQuantity*quantityFrogs)/100
percentMouses = (totalQuantity*quantityMouses)/100

print("Final Report : ")
print("Total of guinea pigs :", totalQuantity)
print("Total of rabbits :", quantityRabbits)
print("Total of mouses :", quantityMouses)
print("Total of frogs :", quantityFrogs)
print("Percentage of rabbits :", percentRabbits, "%")
print("Percentage of mouses :", percentMouses, "%")
print("Percentage of frogs :", percentFrogs, "%")