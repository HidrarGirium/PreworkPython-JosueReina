'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''

edad = int(input('Iserte su edad: '))

if edad >= 18:
  print('Usted es mayor de edad.')
elif edad < 18:
  print('Usted es menor de edad.')