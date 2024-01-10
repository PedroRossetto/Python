M = int(input("Digite quantas linhas a matriz vai ter: "))
N = int(input("Digite quantas colunas a matriz vai ter: "))

# Inicialize a matriz corretamente
matrix = [[0 for x in range(N)] for x in range(M)] 

for i in range(M):
    for j in range(N):
        matrix[i][j] = int(input(f"Elemento [{i},{j}]: ")) 

print("\nMATRIZ DIGITADA:") #\n dá um espaço antes 
for i in range(M):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()
