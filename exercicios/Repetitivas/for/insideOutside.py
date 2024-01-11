# Problema "dentro_fora" (adaptado de URI 1072)
# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
# conforme exemplo
dentro = 0
fora = 0
N = int(input("Enter a quantity of numbers : "))

for i in range (N):
    i+=1
    if(i!=N+1):
        x = int(input("Enter any number : "))
        if(x >= 10 and x <= 20):
         dentro +=1
        else:
         fora +=1
           
           
print(dentro, "inside")
print(fora, "outside")
    
 