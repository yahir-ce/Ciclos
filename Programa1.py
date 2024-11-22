'''
Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)

'''

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
numero = int(input("Introduce un numero para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial( numero )}") 