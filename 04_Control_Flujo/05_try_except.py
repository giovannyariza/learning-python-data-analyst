def calcular_promedio_metrico(lecturas: list[float | int]) -> float | None:
  """
  Calcula el promedio aritmético de una lista de mediciones numéricas.    
  Retorna el promedio como float, o None si la operación no es viable.
  """
  # Verificación preventiva (Manejo de flujo normal)
  if not lecturas:
    print("Advertencia: La lista de lecturas está vacía.")
    return None
  
  # El código que queremos ejecutar y que sospechamos que podría fallar.
  try:
    # Intentamos realizar la operación de agregación
    suma_total: float = sum(lecturas)
    promedio: float = suma_total / len(lecturas)
  
  # La red de seguridad: Captura siempre una excepción específica (nunca uses un 
  # except genérico sin tipo, ya que ocultaría errores de sintaxis o de lógica)
  # Captura errores de tipo (ej: si hay un string mezclado en la lista)
  except TypeError as error:
    print(f"Error de Datos: Todos los elementos deben ser numéricos. Detalle: {error}")
    return None
  
  # Aunque lo prevenimos con el 'if not lecturas', es una buena práctica de respaldo
  except ZeroDivisionError:
    print("Error Matemático: Intento de división por cero.")
    return None
  
  # El bloque que sólo se ejecuta si el código dentro del try no lanzó ninguna excepción
  else:
    print("Cálculo de promedio completado exitosamente.")
    return promedio
  
  # El bloque de limpieza, se ejecuta siempre, haya ocurrido un error o no. Es crucial 
  # para liberar recursos, como cerrar conexiones a bases de datos o archivos abiertos
  finally:
    print("Operación de diagnóstico finalizada.")

# ------------------------------------------------------------------------------

# Caso 1: Datos Limpios
datos_ok: list[float | int] = [120.5, 118.4, 122.1]
resultado_1 = calcular_promedio_metrico(datos_ok)
print(f"Resultado 1: {resultado_1}\n")

# Caso 2: Datos Corruptos (Provoca TypeError intencional al mezclar un string)
datos_corruptos: list[any] = [120.5, "ERROR_SEÑAL", 122.1]
resultado_2 = calcular_promedio_metrico(datos_corruptos)
print(f"Resultado 2: {resultado_2}\n")