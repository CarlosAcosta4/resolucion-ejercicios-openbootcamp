import os
os.system('cls')


def yearBisiesto(year):
    if year % 4 != 0: 
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 != 0:
        print("Es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: 
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
        print("Es bisiesto")


year = int(input('Ingrese un año ----> '))
yearBisiesto(year)