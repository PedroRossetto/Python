# Problema "aumento" (adaptado de URI 1048)
# Uma empresa vai conceder um aumento percentual de
# salário aos seus funcionários dependendo de quanto
# cada pessoa ganha, conforme tabela ao lado. Fazer um
# programa para ler o salário de uma pessoa, daí mostrar
# qual o novo salário desta pessoa depois do aumento,
# quanto foi o aumento e qual foi a porcentagem de
# aumento.

salary = float(input("Enter the salary : "))

if salary <= 1000.00 and salary > 0:
    increase = (salary/100)*20
    totalSalary = salary+increase
    print(f"New salary : ${totalSalary:.2f}")
    print(f"Increase : {increase:.2f}")
    print("Percentage : 20%")
elif salary > 1000.00 and salary < 3000 :
    increase = (salary/100)*15
    totalSalary = salary+increase
    print(f"New salary : ${totalSalary:.2f}")
    print(f"Increase : {increase:.2f}")
    print("Percentage : 15%")
elif salary > 3000 and salary < 8000 :
    increase = (salary/100)*10
    totalSalary = salary+increase
    print(f"New salary : ${totalSalary:.2f}")
    print(f"Increase : {increase:.2f}")
    print("Percentage : 10%")
elif salary > 8000:
    increase = (salary/100)*5
    totalSalary = salary+increase
    print(f"New salary : ${totalSalary:.2f}")
    print(f"Increase : {increase:.2f}")
    print("Percentage : 5%")
else :
    print("Incorrect salary")