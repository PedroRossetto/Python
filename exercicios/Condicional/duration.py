# Problema "tempo_de_jogo" (adaptado de URI 1046) 
# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do
# jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora # máxima de 24 horas.

start = int(input("Enter the time of start game : "))
end = int(input("Enter the time of end game : "))

if start < 0 or end < 0 :
    print("Incorrect time")
elif start > end :
    duration = 24-start+end
    print(duration)
elif start == 0 and end == 0 :
    print("24")
elif start < end :
    duration = -start+end
    print(duration)
else:
    print("Incorrect information")
