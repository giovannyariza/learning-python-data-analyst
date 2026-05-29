# `input()` siempre devuelve una cadena. La anotación `:str` indica el tipo esperado
# Se agrega un espacio al final de la cadena, por convención PEP 8
operator_badge:str = input('Enter technician operator badge ID:\n')

# Si el operador escribe texto no numérico, se lanzará `ValueError`
well_test_duration_hours:int = int(input('Enter well test duration (in hours): '))

# Cálculo de las horas restantes del turno operativo
remaining_shift_hours:int = 12 - well_test_duration_hours

print(f'Operator {operator_badge}, there are approximately {remaining_shift_hours} hours left in your shift.')

# ------------------------------------------------------------------------------

# 1. EVALUACIÓN DE PARÁMETROS DE SEGURIDAD (Presión del Cabezal)
# Solicitamos la presión actual del cabezal del ppozo
wellhead_pressure_psi:float = float(input('Enter current Wellhead Pressure (PSI): '))

# Estructura condicional: evalúa si la presión excede el límite de seguridad
if wellhead_pressure_psi >= 3500.0:
  print('CRITICAL ALERT: High pressure detected! Triggering Automated Choke Valve.')
else:
  print('Operation Normal: Wellhead pressure is within safe operating limits.')

# ------------------------------------------------------------------------------

# 2. ANÁLISIS DE RESIDUOS Y ASIMETRÍA EN CILINDROS DE BOMBEO
# Se solicita el número de carrera o ciclo del pistón de bombeo mecánico (Pump Stroke Count)
stroke_cycle_id:int = int(input('Enter current pump stroke cycle ID to analyze balance:\n'))

# El operador módulo (%) devuelve el residuo de la división entera.
# Identificar si el ciclo actual es un ciclo impar (Upstroke / carrera ascendente) 
# o par (Downstroke / carrera descendente) es vital para el análisis de cargas en la varilla.
if stroke_cycle_id % 2 != 0:
  print(f'Cycle {stroke_cycle_id} is an UPSTROKE (fluid is being lifted to surface).')
else:
  print(f'Cycle {stroke_cycle_id} is a DOWNSTROKE (pump plunger is resetting).')