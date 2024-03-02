# Ejercicio 5: Suma de Números Pares
# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
# Inicializar la variable para almacenar la suma
suma_pares = 0

# Iterar sobre los números del 1 al 100
for numero in range(1, 101):
    # Verificar si el número es par
    if numero % 2 == 0:
        # Sumar el número par a la variable de suma
        suma_pares += numero

# Mostrar el resultado
print(f"La suma de todos los números pares del 1 al 100 es: {suma_pares}")
