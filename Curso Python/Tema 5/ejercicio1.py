import os
os.system('cls')

from math import pi


def areaTriangulo(altura, base):
    return ((altura * base)/ 2)

def areaCirculo(radio):
    return (pi * (radio ** 2))

print('----------ÁREA DE UN TRIÁNGULO----------')
altura = float(input('Ingrese la altura ---> '))
base = float(input('Ingrese la base --->'))

print('\nEl área del Triángulo es : ',areaTriangulo(altura, base) )

print('\n-----------ÁREA DE UN CIRCULO-----------')
radio = float(input('Ingrese el radio ---> '))

print('\nEl área del Circulo es : ',areaCirculo(radio) )