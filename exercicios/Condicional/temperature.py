# Problema "temperatura"
# Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
# isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
# informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
# duas casas decimais.

conversor = input("Enter the temperature you want to convert to (F or C): ")
temperature = float(input("Enter the temperature : "))

if conversor.lower() != 'f' and conversor.lower() != 'c' :
    print("Temperatura inválida")
elif conversor.lower() == 'f' :
    temperature = (temperature * 1.8)+32
    print(f"Temperature :  {temperature:.2f} Fº")
else :
    temperature = (temperature-32)/1.8
    print(f"Temperature : {temperature:.2f} Cº")