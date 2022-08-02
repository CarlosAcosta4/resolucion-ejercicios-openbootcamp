import os
os.system('cls')

def numeroPrimo(num):
    contador = 0

    for i in range (1, num + 1):
        if ( num % i == 0):
            contador += 1
        
    if contador == 2:
        return 'Es Primo'
    else:
        return 'No es Primo'

    
numero = int(input('Ingrese un número entero ---> '))

print(numeroPrimo(numero))

