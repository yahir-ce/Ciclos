'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador
'''
acumulador = 0
contador = 0
for _ in range (10):
   numero =  float(input(f"Introduce el numero: "))
   acumulador+=numero
   contador += 1
promedio = acumulador / contador
print(f"El promedio de los 10 numeros es: {promedio} ")