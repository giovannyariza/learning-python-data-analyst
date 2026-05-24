# La estructura más eficiente para búsquedas rápidas mediante una palabra clave 
# en lugar de una posición numérica. Las claves deben ser únicas e inmutables
metricas_sensor:dict[str, float] = {
  'temperatura': 24.5,
  'humedad': 62.1,
  'presion': 1013.2
}

# Acceso directo por clave en lugar de índice (posición)
print(f'La humedad actual es: {metricas_sensor["humedad"]}%')

# Agregar o actualizar un elemento
metricas_sensor['co2'] = 415.8

# ------------------------------------------------------------------------------
# Generar una lista de diccionarios
inventario_sensores:list[dict] = [
  {
    'tag_sensor': 'FT7214',
    'caudal': 145.8,
    'requiere_mantenimiento': False,
    'ubicacion': 'Línea de entrada principal'
  },
  {
    'tag_sensor': 'FT7227',
    'caudal': 92.3,
    'requiere_mantenimiento': True,
    'ubicacion': 'Línea de transferencia'
  },
  {
    'tag_sensor': 'FT72142',
    'caudal': 0.0,
    'requiere_mantenimiento': False
    # 'ubicacion' se omite intencionalmente para prueba de robustez
  }
]

# ------------------------------------------------------------------------------
# Usamos el operador '|' para indicar que 'ubicación' puede ser texto o None
def obtener_ubicacion_segura(sensor:dict) -> str|None:
  '''
  Retorna la ubicación del sensor si existe, de lo contrario devuelve None
  '''
  # Si usas el método get y la clave no existe Python no 'rompe' el script, sólo
  # devolvera None
  return sensor.get('ubicacion')

# ------------------------------------------------------------------------------
def procesar_reporte_sensores(sensores:list[dict]) -> None:
  '''
  Procesa e imprime el estado operativo de cada sensor en la lista
  '''
  print('=== Reporte operativo de Caudales (Tipado Moderno) ===')

  for sensor in sensores:
    tag:str = sensor['tag_sensor']
    caudal:float = sensor['caudal']

    # Obtenemos el valor y asignamos una contingencia si es None
    ubicacion_detectada:str|None = obtener_ubicacion_segura(sensor)
    zona:str = ubicacion_detectada if ubicacion_detectada is not None else 'Zona no especificada'
    estado:str = 'REQUIERE INTERVENCIÓN' if sensor['requiere_mantenimiento'] else 'OPERATIVO OK'

    print(f'Sensor: {tag} | Caudal: {caudal} m3/h | Ubicación: {zona} | Estado: {estado}')

# ------------------------------------------------------------------------------

# Ejecución del proceso
procesar_reporte_sensores(inventario_sensores)
