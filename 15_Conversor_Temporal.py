'''
Ejercicio 15: Conversor de Tiempo. Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''
def convertir_horas_y_minutos(minutos):
  horas = minutos // 60
  minutos_residuales = minutos % 60
  
  
  print(f'{minutos} minutos son {horas} y {minutos_residuales} minutos')

minutos_input = int(input('Inserte la cantidad de minutos: '))
convertir_horas_y_minutos(minutos_input)
