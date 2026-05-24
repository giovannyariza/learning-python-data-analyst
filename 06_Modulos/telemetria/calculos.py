# Módulo de Lógica Funcional Analítica
# Usamos el tipado moderno indicando que el módulo espera instancias de la otra clase

from telemetria.sensores import InstrumentoMedicion

def obtener_sensores_criticos(lista_sensores:list[InstrumentoMedicion], umbral_porcentaje:float) -> list[InstrumentoMedicion]:
  """
  Filtra y retorna los sensores que superan un porcentaje de saturación específico.
  Aplica una List Comprehension idiomatica (Fase 2).
  """
  return [
    sensor for sensor in lista_sensores 
    if (sensor.valor_actual / sensor.limite_maximo) * 100.0 > umbral_porcentaje
  ]

# ------------------------------------------------------------------------------

if __name__ == "__main__":
  print("--- [MODO PRUEBA] Ejecutando calculos.py directamente ---")
  # Este bloque fallaría si se ejecuta solo, ya que depende de la estructura del paquete