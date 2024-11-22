'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio

print(f"Números pares entre {inicio} y {fin}:")

for num in range(inicio, fin + 1):
    if num % 2 == 0:
        print(num)