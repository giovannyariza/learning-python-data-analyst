import sys
import time
# 1. Creamos el GENERADOR (Nuestro asistente perezoso)
# Nota el tipo de retorno: 'Iterator[float]' significa que es un objeto que se puede recorrer uno a uno
from collections.abc import Iterator


def simulador_lector_gigante(total_lineas:int) -> Iterator[float]:
  """
  Simula la lectura de un archivo gigantesco línea por línea.
  Entrega una medición a la vez sin llenar la memoria RAM.
  """
  print(f"\n[Generador] Abriendo el saco virtual con {total_lineas} registros...")
  
  for i in range(1, total_lineas + 1):
    # Simulamos que calculamos o leemos una temperatura del archivo
    temperatura_simulada:float = 20.0 + (i * 0.001)
    
    # ¡LA MAGIA! En lugar de 'return', usamos 'yield'.
    # Entregamos este número y la función se congela aquí mismo.
    yield temperatura_simulada
      
  print("[Generador] Se han terminado todos los registros del saco.")

# ------------------------------------------------------------------------------

# 2. El programa principal (El Chef)
def main() -> None:
  print("=== INICIANDO PRUEBA DE EFICIENCIA DE MEMORIA ===")
  
  # Queremos procesar 5 millones de registros de telemetría
  TOTAL_REGISTROS:int = 5_000_000
  
  # CREAMOS EL ASISTENTE: 
  # Ojo: Aquí la función NO se está ejecutando. Solo estamos instanciando el generador.
  asistente_saco = simulador_lector_gigante(TOTAL_REGISTROS)
  
  # PRUEBA DE MEMORIA: Vamos a ver cuánto pesa este asistente en la RAM
  peso_en_ram:int = sys.getsizeof(asistente_saco)
  print(f"-> Peso del generador en la memoria RAM: {peso_en_ram} bytes.")
  print("Nota: ¡Ocupa aproximadamante 200 bytes de RAM para controlar 5 millones de datos!")
  
  print("\n--- Iniciando procesamiento uno a uno ---")
  time.sleep(1) # Pequeña pausa para leer la consola
  
  # Consumimos el generador usando un bucle 'for' tradicional.
  # El 'for' le dice automáticamente al generador: "next()", "next()", hasta que se acabe.
  contador:int = 0
  for temperatura in asistente_saco:
    contador += 1
    
    # Para no inundar tu pantalla, solo imprimimos cada 1 millón de patatas procesadas
    if contador % 1_000_000 == 0:
      print(f" Chef: Procesada la medición número {contador} -> Temperatura actual: {temperatura:.2f} °C")
      print("       (La mesa de la RAM sigue limpia...)")
          
  print(f"\n=== PROCESO TERMINADO: Se procesaron {contador} registros exitosamente ===")

# ------------------------------------------------------------------------------

if __name__ == "__main__":
  main()