# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def es_palindromo(palabra):
    # Convierte la palabra a minúsculas para hacer la comparación sin importar mayúsculas o minúsculas
    palabra = palabra.lower()
    
    # Elimina los espacios en blanco de la palabra
    palabra = palabra.replace(" ", "")
    
    # Compara la palabra original con su reverso
    return palabra == palabra[::-1]

# Solicitar al usuario que ingrese una palabra
entrada_usuario = input("Ingresa una palabra: ")

# Verificar si la palabra es un palíndromo
if es_palindromo(entrada_usuario):
    print(f"{entrada_usuario} es un palíndromo.")
else:
    print(f"{entrada_usuario} no es un palíndromo.")





