'''
Ejercicio 7: Calculadora Simple. Crea un programa que realice operaciones aritméticas simples (suma, resta,multiplicación, división) según la elección del usuario.
'''

while True:
  num1 = input('Ingrese el primer número: ')
  num2 = input('Ingrese el segundo número: ')
  try:
    num1 = float(num1)
    num2 = float(num2)
    break
  except ValueError:
    print('Carácter no válido, inserte un número')
    
while True:
  print('Utilice: "S" (Suma), "R" (Resta), "M" (Multiplicación), "D" (División) para operar.')
  print(f'\n')
  operador = input('Inserte un operador: ').upper()
  try:
    operador = int(operador)
    break
  except ValueError:
    print('Carácter no válido, inserte: S / R / M / D')

if operador == 'S':
  suma = float(num1) + float(num2)
  print(f'El resultado es {suma}')
elif operador == 'R':
  resta = float(num1) - float(num2)
  print(f'El resultado es {resta}')
elif operador == 'M':
  mult = float(num1) * float(num2)
  print(f'El resultado es {mult}')
elif operador == 'D':
  div = float(num1) / float(num2)
  print(f'El resultado es {div}')