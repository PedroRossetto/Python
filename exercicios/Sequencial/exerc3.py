# Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
# nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo.

name1 = input("Digite seu nome : ")
age1 = int(input("Digite sua idade : "))
name2 = input("Digite seu nome : ")
age2 = int(input("Digite sua idade : "))


print("A primeira pessoa se chama", name1, "e tem :", age1 ," anos")

print("A segunda pessoa se chama", name2, "e tem :", age2 , " anos")

media = ((age1+age2)/2)

print("A média das idades deles é : ", media)

# Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes
# numeros

val1 = int(input("Digite um valor : "))
val2 = int(input("Digite outro valor : "))
print("A soma dos dois valores é igual a : ", val1+val2)