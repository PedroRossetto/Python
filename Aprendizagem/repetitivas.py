#Precisa mostrar que horas são e quantas horas faltam para chegar ás 18

exactTime = int
exactTime = 18
hoursLeft = int

currentTime = int(input("Que horas são? : "))

if (currentTime <= exactTime) :
    while currentTime < exactTime:
        hoursLeft = exactTime - currentTime
        print("São : ", currentTime, "horas")
        print("Faltam : ", hoursLeft, "horas")
        currentTime = currentTime + 1
        
        
        
        if (currentTime == exactTime) :
            print("Chegou a hora! São 18 horas")
elif(currentTime > exactTime) :
    print("O horário já passou, você está atrasado")
    