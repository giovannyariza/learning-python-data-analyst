# En Python, la toma de decisiones se basa en una regla de oro llamada indentación

# Constantes de configuración (Límites de operación)
# Cuando se trabajae con umbrales o límites, nunca escribirlos directamente en la
# condición o comparación (a esto se llama hardcoding)
LIMITE_CRITICO:float = 1200.0
LIMITE_ADVERTENCIA:float = 1000.0

def evaluar_presion(presion_actual:float) -> str:
  '''
  Evalua la presión actual y retorna el nivel de alerta correspondiente
  '''
  # Condición más restrictiva primero
  if presion_actual > LIMITE_CRITICO: # La condición termina con :
    return 'CRÍTICO: Parada de emergencia requerida.'  
  # Condición intermedia
  elif presion_actual > LIMITE_ADVERTENCIA:
    return 'ADVERTENCIA: Monitorear de cerca.'
  # Caso por defecto si ninguna de las anteriores se cumple
  else:
    return 'NORMAL: Operación segura.'

# ------------------------------------------------------------------------------

# Ejecución de prueba
estado:str = evaluar_presion(1050.5)

print(estado) # Salida: ADVERTENCIA: Monitorear de cerca.