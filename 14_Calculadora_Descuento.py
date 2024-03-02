'''
Ejercicio 14: Calculadora de Descuento. Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
'''

precio = float(input('Ingrese al precio total de la compra: '))

descuento = precio * 0.2

precio_final = precio - descuento

print(f"El total de su compra es: {precio_final:.2f}")