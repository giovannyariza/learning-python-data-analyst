# Uso del módulo asyncio
import asyncio
# Usado para verificación de timpo de ejecución del script
import time

# Corrutina de bajo nivel
async def consultar_api_estacion(tag_estacion:str, latencia_segundos:float) -> dict:
  """
  Simula una petición HTTP asíncrona a la API de una estación de producción.
  """
  print(f'[{tag_estacion}] -> Iniciando consulta de telemetría vía API...')

  # Ceder el control al Event Loop de forma obligatoria durante la espera de red
  await asyncio.sleep(latencia_segundos)

  # Datos simulados de retrono una vez que la API responde
  print(f'[{tag_estacion}] <- Datos recibidos exitosamente.')
  return {
    "estacion": tag_estacion,
    "estado_valvulas": "OK",
    "timestamp_registro": time.time()
  }

# ------------------------------------------------------------------------------

# Corrutina de alto nivel (Orquestador)
async def main() -> None:
  """
  Configura las tareas concurrentes y consolida las respuestas de la red.
  """
  print("=== Iniciando consumo Asincronía de Datos ===")
  tiempo_inicio:float = time.perf_counter() # Inicia contador de rendimiento

  # 1. Definimos las llamadas a las API simuladas, no se ejecutan aun.
  tarea_alfa:dict = consultar_api_estacion("ESTACIÓN ALFA", 2.0)
  tarea_bravo:dict = consultar_api_estacion("ESTACIÓN BETA", latencia_segundos=1.5)
  tarea_charlie:dict = consultar_api_estacion(latencia_segundos=2.5, tag_estacion="ESTACIÓN CHARLIE")

  # 2. Inyectamos el lote de tareas al Event Loop para ejecución concurrente
  print('\n[Evento Loop] Disparanco consultas en paralelo...')

  # asyncio.gather empaqueta las promesas y espera a que todas terminen
  # Si alguna consulta falla, el parámetro return_exceptions=True permitirá retornar 
  # las consultas exitosas sin abortar todo el bloque
  resultados:list[dict] = await asyncio.gather(tarea_alfa, tarea_bravo, tarea_charlie, return_exceptions=True)

  print('\n[Evento Loop] Todas las consultas de red han finalizado.')

  # 3. Procesamiento de los resultados consolidados
  for reporte in resultados:
    print(f" -> Procesando métricas de {reporte['estacion']} | Estado: {reporte['estado_valvulas']}")
  
  tiempo_total:float = time.perf_counter() - tiempo_inicio

  print(f"\n=== PROCESO COMPLETADO EN: {tiempo_total:.2f} SEGUNDOS")
  print("Nota: Si fuera síncrono, el tiempo total habría sido de 6.00 segundos.")

# ------------------------------------------------------------------------------

# Punto de entrada adaptado para entornos asíncronos
if __name__ == "__main__":
  # Inicializa el bucle de eventos nativo y ejecuta la corrutina principal
  asyncio.run(main())