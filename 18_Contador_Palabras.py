'''
Ejercicio 18: Contador de Palabras. Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
def contar_palabras(oracion):
    # Dividir la oración en palabras usando el espacio como delimitador
    palabras = oracion.split()
    
    # Contar la cantidad de palabras
    cantidad_palabras = len(palabras)
    
    return cantidad_palabras

# Pedir al usuario que ingrese una oración
oracion_usuario = input("Ingresa una oración: ")

# Llamar a la función y mostrar el resultado
resultado = contar_palabras(oracion_usuario)
print(f"La cantidad de palabras en la oración es: {resultado}")

