# Python no tiene un condicional switch tradicional. En su lugar, introdujo match-case 
# (Coincidencia de Patrones Estructurales). No es solo un reemplazo estético de if-else; 
# permite evaluar la estructura y el tipo de los datos de manera mucho más limpia.

def mapear_codigo_error(codigo: int) -> str:
  """
  Asocia un código numérico con su descripción operativa usando match-case.
  """
  match codigo:
    case 200:
      return "Conexión exitosa con el sensor."
    case 404:
      return "Error: Sensor no localizado en la red."
    case 500:
      return "Error Interno: Falla de telemetría."
    case _:  # Caso por defecto para cualquier otro código
      return f"Código {codigo} desconocido. Requiere revisión manual."

# ------------------------------------------------------------------------------

# Ejecución de prueba
print(mapear_codigo_error(404))  # Salida: Error: Sensor no localizado en la red.