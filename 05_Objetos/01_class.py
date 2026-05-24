# Una clase es simplemente un plano arquitectónico o un molde, no contiene datos reales.
# Define que características tendrá el objeto (atributos) y que acciones puede realizar
# (métodos)

class InstrumentoMedicion:
  # Optimización senior: Fija los atributos en memoria y acelera la ejecución
  __slots__ = ('tag', 'valor_actual', 'limite_maximo')

  # El constructor, su único trabajo es inicializar los atributos del objeto
  def __init__(self, tag:str, valor_inicial:float, limite_maximo:float) -> None:
    """
    Inicializa un nuevo instrumento de medición con sus umbrales operativos.
    """
    self.tag:str = tag # self, representa la misma instancia
    self.valor_actual:float = valor_inicial
    self.limite_maximo:float = limite_maximo


  def actualizar_lectura(self, nueva_lectura: float) -> None:
    """
    Actualiza el valor actual medido por el instrumento.
    """
    if nueva_lectura < 0:
      print(f"[{self.tag}] Advertencia: Intento de registrar lectura negativa: {nueva_lectura}")
    self.valor_actual = nueva_lectura


  def verificar_alarma(self) -> bool:
    """
    Evalúa si la lectura actual supera el límite máximo de seguridad.
    """
    return self.valor_actual > self.limite_maximo

# ------------------------------------------------------------------------------

# Una instancia es el objeto real construido a partir de ese molde, viviendo en la memoria
# RAM con sus propios datos específicos

# 1. Creamos dos instancias (objetos reales e independientes en memoria)
sensor_presion = InstrumentoMedicion(tag="PT_7214", valor_inicial=1150.0, limite_maximo=1200.0)
sensor_temperatura = InstrumentoMedicion(tag="TT_3012", valor_inicial=45.2, limite_maximo=85.0)

# 2. Operamos de forma independiente sobre cada objeto
print(f"Estado inicial {sensor_presion.tag}: {sensor_presion.valor_actual} PSI")

# Actualizamos la lectura del sensor de presión para forzar una alarma
sensor_presion.actualizar_lectura(1230.5)

# 3. Evaluamos las alarmas de cada uno
print(f"¿Alarma en {sensor_presion.tag}?: {sensor_presion.verificar_alarma()}") # Salida: True
print(f"¿Alarma en {sensor_temperatura.tag}?: {sensor_temperatura.verificar_alarma()}") # Salida: False