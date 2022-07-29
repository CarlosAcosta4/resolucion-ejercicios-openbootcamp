import os
os.system('cls')

def operacion(num1, num2, num3):
    suma = num1 + num2 + num3
    return suma


def aumento(añadirPuertas):
    totalPuertas = 4
    totalPuertas += añadirPuertas
    return totalPuertas


#Programa Principal

#Primer Ejercicio

num1 = int(input('Número 1 ---> '))
num2 = int(input('Número 2 ---> '))
num3 = int(input('Número 3 ---> '))

sumaTotal = operacion(num1, num2, num3)

print('La suma total es ---> ',sumaTotal )

print('---------------------------------------------')

#Segundo Ejercicio

print('Números de puertas iniciales --->', aumento(0))
añadir = int(input('Ingrese el numero de puertas para añadir --->'))
print('Números de puertas totales --->', aumento(añadir))

