'''
Este programa utiliza un bucle for para iterar desde 1 hasta el número ingresado por el usuario (inclusive). En cada iteración, verifica si el número actual es par y, en caso afirmativo, incrementa el contador de números pares. Finalmente, muestra el resultado al usuario.
'''

# Solicitar al usuario que ingrese un número
numero_ingresado = int(input("Ingresa un número: "))

# Inicializar el contador de números pares
contador_pares = 0

# Iterar desde 1 hasta el número ingresado
for i in range(1, numero_ingresado + 1):
    # Verificar si el número actual es par
    if i % 2 == 0:
        # Incrementar el contador de números pares
        contador_pares += 1

# Mostrar el resultado
print(f"Entre 1 y {numero_ingresado}, hay {contador_pares} números pares.")

