# Ejercicio 11: Calculadora de Edad. Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

birth_year = int(input('Ingrese el su año de nacimiento: '))
print('\n')

current_year = int(input('Ingrese el año actual en transcurso: '))
print('\n')

edad = current_year - birth_year

print(f'Su edad es de {edad} años.')
