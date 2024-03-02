'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''
listanumeros = []
numerousuario = int(input('Inserte un número: '))
listanumeros.append(numerousuario)
decision = input('¿Desea añadir más números? (S/N): ')

while decision == 's' or decision == 'S':
  numerousuario = int(input('Inserte un número: '))
  listanumeros.append(numerousuario)
  decision = input('¿Desea añadir más números? (S/N): ')

print(f'Los números introducidos son: {listanumeros}')
cont_par = 0
cont_impar = 0

for x in listanumeros:
  if x % 2 == 0:
    cont_par += 1
  elif x % 2 != 0:
    cont_impar +=1
  
print(f'Ha insertado un total de {cont_par} números par y {cont_impar} números impares')


input('Por favor, presione una tecla para salir')
