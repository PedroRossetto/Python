# Problema "notas"
# Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
# uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
# ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
# mensagem "REPROVADO", conforme exemplos.

grade1 = float(input("Enter the people first grade : "))
grade2 = float(input("Enter the people second grade : "))

avarageGrade = (grade1+grade2)/2

print(f"Your final grade : {avarageGrade:.2f}")

if (avarageGrade > 60):
    print("Approved")
elif (avarageGrade < 0):
    print("IMPOSSIBLE")
else :
    print("Dissaproved")
    
