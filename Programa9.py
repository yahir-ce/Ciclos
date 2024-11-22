'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''
while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))
    if limite_inferior < limite_superior:
        break
    print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")

suma_dentro = 0
fuera_intervalo = 0
igual_a_limites = False

print("Introduce números (0 para terminar):")
while True:
    numero = int(input("> "))
    if numero == 0:
        break
    if limite_inferior < numero < limite_superior: 
        suma_dentro += numero
    elif numero <= limite_inferior or numero >= limite_superior:
        fuera_intervalo += 1
    if numero == limite_inferior or numero == limite_superior:
        igual_a_limites = True

print("\nResultados:")
print(f"1. La suma de los números dentro del intervalo es: {suma_dentro}")
print(f"2. Cantidad de números fuera del intervalo: {fuera_intervalo}")
print(f"3. ¿Se introdujo algún número igual a los límites?: {'Sí' if igual_a_limites else 'No'}")