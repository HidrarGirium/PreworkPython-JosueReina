'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''

print('Calculadora Celsius a Fahrenheit')
print()
while True:
  C = input('Inserte la temperatura en Celsius:')
  try:
    C = float(C)
    break
  except ValueError:
    print('Carácter no válido, inserte un número')
    print()
    
while True:
    C = float(C)
    F = C + 32
    print(f'{C:.1f}ºC es igual a {F:.1f}ºF')
    print()
    break

print('Fin del programa')


