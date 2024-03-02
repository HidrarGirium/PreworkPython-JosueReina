# Ejercicio 9: Conversor de Divisas. Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.

usd = float(input('Ingrese la cantidad de USD que quiere convertir a EUR: '))
eur = usd * 0.85
print()
print(f'{usd:.2f} USD equivalen a {eur:.2f} EUR')
print('Fin del programa')