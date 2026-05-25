from concurrent.futures import ProcessPoolExecutor
import os
import time


def operacion_matematica_pesada(id_lote: int) -> int:
  """
  Simula un algoritmo analítico pesado (CPU Bound) que requiere alta capacidad de cómputo.
  """
  # Identificamos qué proceso del sistema operativo está resolviendo esta tarea
  pid_actual:int = os.getpid()
  print(f"[Proceso PID: {pid_actual}] Iniciando procesamiento del lote analítico: {id_lote}...")
  
  # Simulación de estrés algorítmico (bucle de alto consumo de CPU)
  contador:int = 0
  for i in range(15_000_000):
    contador += (i % 3)
      
  print(f"[Proceso PID: {pid_actual}] FInalizó procesamiento del lote: {id_lote}.")
  return contador

# ------------------------------------------------------------------------------

def main() -> None:
  """
  Orquesta la distribución de las cargas matemáticas en los núcleos del procesador.
  """
  print("=== CONFIGURANDO ENTORNO DE CÓMPUTO PARALELO ===")
  
  # Detectamos la arquitectura física de la máquina actual
  nucleos_disponibles:int = os.cpu_count() or 1
  print(f"Núcleos de CPU detectados en este hardware: {nucleos_disponibles}")
  
  # Creamos un lote de 4 tareas pesadas para procesar
  lotes_de_datos:list[int] = [1, 2, 3, 4]
  
  tiempo_inicio:float = time.perf_counter()
  
  # Inicializamos el Pool de procesos de forma segura usando un Context Manager ('with')
  # max_workers se ajusta automáticamente al hardware si se deja vacío, o podemos forzarlo
  with ProcessPoolExecutor(max_workers=nucleos_disponibles) as ejecutor:
    print("\n[Executor] Distribuyendo tareas uniformemente entre los procesos hijos...")
    
    # .map() divide la lista 'lotes_de_datos' y la envía a los núcleos en paralelo
    # Bloquea la ejecución del hilo principal hasta que todos los subprocesos terminen
    resultados_iterador = ejecutor.map(operacion_matematica_pesada, lotes_de_datos)
    
    # Convertimos el iterador a una lista nativa para consolidar las respuestas
    resultados:list[int] = list(resultados_iterador)
      
  print("\n[Executor] Todos los subprocesos han devuelto sus datos a la memoria central.")
  print(f"Resultados consolidados de la analítica: {resultados}")
  
  tiempo_total: float = time.perf_counter() - tiempo_inicio
  print(f"\n=== COMPUTACIÓN PARALELA FINALIZADA EN: {tiempo_total:.2f} SEGUNDOS ===")

# ------------------------------------------------------------------------------

# GUARDiÁN CRÍTICO: Obligatorio para evitar ejecuciones infinitas en multiprocesamiento
if __name__ == "__main__":
  main()