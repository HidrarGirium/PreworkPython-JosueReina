'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''
while True:
  try:
    coste = float(input('Inserte el coste del servicio: '))
    print()
  except ValueError:
    print('ERROR: Inserta sólo números')
  if coste <= 0:
    print('ERROR: Inserte una cantidad mayor que cero')
  else:
    break

propina = coste * 0.15
total = coste + propina
print(f'El total es: {total:.2f}')
print('Gracias')
