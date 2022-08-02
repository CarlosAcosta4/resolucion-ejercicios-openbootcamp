import os
os.system('cls')

numero_inicial =  int(input( 'Introduce un número inicial : '))
numero_final =  int(input( 'Introduce un número final : ' ))
numeros_impares = []


while numero_final <= numero_inicial:
    print('El número final debe ser mayor que el número inicial, vuelva a intentarlo')
    numero_inicial =  int(input( 'Introduce un número inicial : '))
    numero_final =  int(input( 'Introduce un número final : ' ))
    
else:
    for num in range(numero_inicial, numero_final + 1 ):
            if (num % 2 != 0):
                numeros_impares.append(num)

print('---------------Números Impares---------------')
print(numeros_impares)
