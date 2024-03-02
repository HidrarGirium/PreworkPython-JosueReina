'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Pedir al usuario que ingrese un año
try:
    year_usuario = int(input("Ingresa un año: "))
    
    # Verificar si el año es bisiesto o no
    if es_bisiesto(year_usuario):
        print(f"{year_usuario} es un año bisiesto.")
    else:
        print(f"{year_usuario} no es un año bisiesto.")
except ValueError:
    print("Por favor, ingresa un año válido.")