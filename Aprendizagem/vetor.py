N = int

N = int(input("Digite quantos numeros você quer digitar : "))

meu_vetor : [int] = [0 for x in range(N)]

for i in range(0, N):
    meu_vetor[i] = float(input("Digite o valor : "))
    
    
print()
print("NUMEROS DIGITADOS : ")
for i in range (0, N):
    print(f"{meu_vetor[i]:.1f}")