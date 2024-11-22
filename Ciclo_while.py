'''
Rstructura while

while exp_bool:
   instrucciones
   actualiza valor para exp_bool

'''

##Tabla de multiplicar
num = int(input("Escribe un numero: "))
i = 1
while i <= 10:
    print(f"{ num } * { i } = {num * i }")
    i = i + 1

''' 
1234
'''
#Programa que sale hasta decirle salir

while True:
    option = input("Escribe salir: ")
    if option == 'Salir':
        break