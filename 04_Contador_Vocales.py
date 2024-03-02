'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''
def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador_vocal = 0

    for letra in palabra:
        if letra in vocales:
            contador_vocal += 1

    return contador_vocal

# Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingresa una palabra: ")

# Contar el número de vocales en la palabra ingresada
numero_vocales = contar_vocales(palabra_ingresada)

# Mostrar el resultado
print(f"El número de vocales en '{palabra_ingresada}' es: {numero_vocales}")



