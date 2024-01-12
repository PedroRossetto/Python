# Problema "dados_pessoas"
# Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
# que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
# de homens.
n = int(input("Enter a number of peoples : "))

alturas = [0 for x in range (n)]
gender = [0 for x in range (n)]

numberGirls = 0
numberBoys = 0


for i in range (n):
    alturas[i] = float(input("Enter a height : "))
    y = input("Gender : ")
    if y.lower()=="f":
            numberGirls+=1
            gender[i]=y.upper()
    elif y.lower()=="m":
            numberBoys+=1
            gender[i]=y.upper()
    else:
        print("Gender Incorrect")
        break

girlsHeight = []


for j in range (n):
    if (gender[j] == "F"):
        girlsHeight.append(alturas[j]) 
        
lessHeight = min(alturas)
greaterHeight = max(alturas)


        
avarageGirlsHeight = 0

for height in girlsHeight:
    avarageGirlsHeight+=height

if numberGirls>0:
    avarageGirlsHeight = avarageGirlsHeight/numberGirls


print("Less height is : ", lessHeight)
print("Greater height is :", greaterHeight)
print("The avarage girls height is: ", avarageGirlsHeight)
print("The number of boys is :", numberBoys)