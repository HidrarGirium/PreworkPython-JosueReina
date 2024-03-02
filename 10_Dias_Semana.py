'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
while True:
  
  try:
    dia_ingresado = int(input('Inserte el número del día de la semana que es hoy: '))
  except ValueError:
    print('ERROR: Inserte un número del 1 al 7')
  if dia_ingresado == 1:
    print('Hoy es lunes!')
    break
  elif dia_ingresado == 2:
    print('Hoy es martes!')
    break
  elif dia_ingresado == 3:
    print('Hoy es miercoles!')
  elif dia_ingresado == 4:
    print('Hoy es jueves!')
    break
  elif dia_ingresado == 5:
    print('Hoy es viernes!')
    break
  elif dia_ingresado == 6:
    print('Hoy es sábado!')
    break
  elif dia_ingresado == 7:
    print('Hoy es domingo!')
    break
  else:
    print('Creo que no has entendido mi pregunta. Indica un día de la semana del numero 1 al 7')