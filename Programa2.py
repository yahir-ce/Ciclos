'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
nu= numero del usuario
na= numero para adivinar
ir= intentos restantes


'''

import random


na = random.randint(1, 100)
intentos = 10

print("¡Bienvenido al juego de adivinar el numero!")
print("Tienes 10 intentos para adivinar el numero entre 1 y 100.")

for i in range(1, intentos + 1):
    
    try:
        nu = int(input(f"Intento {i}. Introduce un numero: "))
    except ValueError:
        print("Por favor, introduce un numero valido.")
        continue

    
    if nu == na:
        print(f"¡Felicidades! Has adivinado el número en {i} intentos.")
        break
    elif nu < na:
        print("El numero a adivinar es mayor.")
    else:
        print("El numero a adivinar es menor.")

    
    ir = intentos - i
    if ir > 0:
        print(f"Te quedan {ir} intentos.")
    else:
        print(f"Lo siento, te has quedado sin intentos. El número era {na}.")