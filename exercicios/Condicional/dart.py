# Problema "dardo"
# No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
# Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
# foi a maior.

firstJT = float(input("Enter the distance of first dart : "))
secondJT = float(input("Enter the distance of second dart : "))
thirdJT = float(input("Enter the distance of third dart : "))


if firstJT < 0 or secondJT < 0 or thirdJT < 0 :
    print("PLAY STRAIGHT  !!!  😒👌")
elif firstJT > secondJT and firstJT > thirdJT :
    print("The first dart went further!!!")
elif secondJT > firstJT and secondJT > thirdJT :
    print("The second dart went further!!!") 
elif thirdJT > firstJT and thirdJT > secondJT :
    print("The third dart went further!!!") 
elif firstJT == secondJT and firstJT == thirdJT :
    print("All darts went further!!!")
elif firstJT == secondJT :
    print("The first and second dart went further!!!")
elif firstJT == thirdJT :
    print("The first and third dart went further!!!")
else :
    print("The second and third dart went further!!!")
    
    
