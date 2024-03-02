'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC). Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
(IMC = peso (kg)/ [estatura (m)]2
'''

# Preguntar al usuario que indique su peso.
peso = float(input('Inserte su peso en kilogramos: '))
print('\n')
# Preguntar al usuario que indique su altura
altura = float(input('Inserte su estatura en metros: '))
print('\n')

# Calcular el IMC

imc = peso / (altura**2)

# Mostrar resultado IMC al usuario

print(f'El indice de masa corporal es de {imc:.2f}')