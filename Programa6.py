'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''
cantidad = int(input("Introduce la cantidad de numeros a introducir: "))

mayores_a_cero = 0
menores_a_cero = 0
iguales_a_cero = 0


for _ in range(cantidad):
    numero = float(input("Introduce un numero: "))
    
    
    if numero > 0:
        mayores_a_cero += 1
    elif numero < 0:
        menores_a_cero += 1
    else:
        iguales_a_cero += 1


print(f"Numeros mayores que 0: {mayores_a_cero} ")
print(f"Numeros menores que 0: {menores_a_cero} ")
print(f"Numeros iguales a 0: {iguales_a_cero} ")