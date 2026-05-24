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

# El bloque for es un iterador potente, no requiere manejar contadores manuales

def procesar_historial_lecturas(lecturas:list[float]) -> None:
  """
  Recorre un lote de lecturas de presión y detiene el proceso si detecta peligro.
  """
  print("Iniciando análisis de lote...")
  
  for lectura in lecturas:
    resultado = evaluar_presion(lectura)
    print(f"Evaluando {lectura} PSI -> {resultado}")
    
    if "CRÍTICO" in resultado:
      print("--- PROCESO ABORTADO POR SEGURIDAD ---")
      break  # Detiene el bucle for inmediatamente

# ------------------------------------------------------------------------------

# Datos de simulación (la tercera lectura disparará la alarma)
registro_presiones:list[float] = [950.0, 1020.0, 1250.8, 980.0]

procesar_historial_lecturas(registro_presiones)