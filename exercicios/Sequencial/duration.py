# Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
# formato horas:minutos:segundos.

duration = int(input("Enter the quantity of seconds : "))

hours = int(duration/60/60)
minutes = int(duration/60)%60
secondsRemaining = duration%60

print("Hours : ", hours)
print("Minutes : ", minutes)
print("Seconds : ", secondsRemaining)