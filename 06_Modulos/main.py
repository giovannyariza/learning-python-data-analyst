# Punto de entrada principal de la aplicación

# Importaciones absolutas limpias
from telemetria.sensores import InstrumentoMedicion
from telemetria.calculos import obtener_sensores_criticos

def ejecutar_sistema() -> None:
  """
  Orquesta la inicialización de la telemetría y ejecuta los análisis modulares.
  """
  print("=== Iniciando Sistema Central de Telemetría ===")
  
  # 1. Creamos la base de datos de objetos (Fase 3/POO)
  red_sensores: list[InstrumentoMedicion] = [
    InstrumentoMedicion(tag="PT_7214", valor_inicial=950.0, limite_maximo=1000.0), # 95% Carga
    InstrumentoMedicion(tag="PT_7215", valor_inicial=400.0, limite_maximo=1000.0), # 40% Carga
    InstrumentoMedicion(tag="TT_3012", valor_inicial=85.0, limite_maximo=100.0)    # 85% Carga
  ]
  
  # 2. Consumimos la función del módulo de cálculos
  UMBRAL_ALERTA: float = 80.0
  anomalías = obtener_sensores_criticos(red_sensores, umbral_porcentaje=UMBRAL_ALERTA)
  
  # 3. Desplegamos resultados
  print(f"\nReporte: Sensores operando por encima del {UMBRAL_ALERTA}% de su capacidad:")
  
  for instrumento in anomalías:
    porcentaje = (instrumento.valor_actual / instrumento.limite_maximo) * 100.0
    print(f" -> Alerta en [{instrumento.tag}]: {instrumento.valor_actual} ({porcentaje:.1f}%)")

# ------------------------------------------------------------------------------

# El Guardián definitivo: Asegura que este script sea el que inició la ejecución
if __name__ == "__main__":
  ejecutar_sistema()