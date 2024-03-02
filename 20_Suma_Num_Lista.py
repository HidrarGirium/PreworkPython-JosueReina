'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Pedir al usuario que ingrese una lista de números separados por espacios
try:
    entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
    
    # Convertir la entrada del usuario a una lista de números
    lista_numeros = [int(x) for x in entrada_usuario.split()]
    
    # Calcular la suma de la lista de números
    resultado = sumar_lista(lista_numeros)
    
    # Mostrar el resultado
    print(f"La suma de los números en la lista es: {resultado}")

except ValueError:
    print("Por favor, ingresa una lista válida de números.")
