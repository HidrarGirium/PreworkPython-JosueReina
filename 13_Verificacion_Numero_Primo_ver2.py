'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo o no.
'''

num = int(input('Inserte un número: '))
if num > 1:
  cont = 0
  i = 2
  while i < num and cont == 0:
    resto = num%i
    print(f'{num} % {i} = {resto}')
    if resto == 0:
      cont += 1
    i += 1
  if cont == 0:
    print(f'El {num} es un número primo')
  else:
    print('El {num} no es un número primo')
else:
  print(f'El {num} no es un número primo')