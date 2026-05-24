class InstrumentoMedicion:
  __slots__ = ('tag', '_valor_actual', 'limite_maximo')


  def __init__(self, tag:str, valor_inicial:float, limite_maximo:float) -> None:
    self.tag:str = tag
    self.limite_maximo:float = limite_maximo
    self.valor_actual:float = valor_inicial


  @property
  def valor_actual(self) -> float:
    return self._valor_actual


  @valor_actual.setter
  def valor_actual(self, nuevo_valor:float) -> None:
    if nuevo_valor < -273.15: # Cero absoluto en Celsius como límite físico mínimo
      raise ValueError(
        f"[{self.tag}] Error Crítico: Temperatura por debajo del cero absoluto."
      )
    if nuevo_valor < 0.0 and not hasattr(self, '_permitir_negativos'):
      # Permite flexibilidad si la subclase redefine esta regla
      raise ValueError(
        f"[{self.tag}] Error Crítico: No se permiten lecturas negativas."
      )
    self._valor_actual = nuevo_valor

  # Propiedad de sólo lectura
  @property
  def porcentaje_saturacion(self) -> float:
    """
    Calcula qué tan cerca está el instrumento de su límite crítico.
    """
    return (self._valor_actual / self.limite_maximo) * 100.0


  def verificar_alarma(self) -> bool:
    return self._valor_actual > self.limite_maximo


  # --- Métodos Mágicos (Dunder) ---
  def __str__(self) -> str:
    """Representación amigable en formato texto."""
    return f"Instrumento {self.tag} | Carga: {self.porcentaje_saturacion:.1f}%"

  def __repr__(self) -> str:
    """Representación técnica detallada para depuración."""
    return f"InstrumentoMedicion(tag='{self.tag}', valor_inicial={self._valor_actual}, limite_maximo={self.limite_maximo})"

  def __eq__(self, otro: object) -> bool:
    """Define si dos instrumentos son operacionalmente equivalentes."""
    if not isinstance(otro, InstrumentoMedicion):
      return NotImplemented
    return self.tag == otro.tag

  def __lt__(self, otro: object) -> bool:
    """Define el criterio de ordenamiento basado en la criticidad (saturación)."""
    if not isinstance(otro, InstrumentoMedicion):
      return NotImplemented
    return self.porcentaje_saturacion < otro.porcentaje_saturacion

# ------------------------------------------------------------------------------

# --- Subclase 1: Transmisor de Presión ---
class TransmisorPresion(InstrumentoMedicion):
  __slots__ = ("unidad",)  # Evita duplicar los slots de la clase padre


  def __init__(self, tag:str, valor_inicial:float, limite_maximo:float, unidad:str = "PSI") -> None:
    # Invocamos al constructor de la superclase
    super().__init__(tag, valor_inicial, limite_maximo)
    self.unidad:str = unidad


  def verificar_alarma(self) -> bool:
    """
    Polimorfismo: Lógica específica para presión.
    """
    return self.valor_actual > self.limite_maximo

# ------------------------------------------------------------------------------

# --- Subclase 2: Transmisor de Temperatura ---
class TransmisorTemperatura(InstrumentoMedicion):
  __slots__ = ("unidad", "_permitir_negativos")

  def __init__(self, tag:str, valor_inicial:float, limite_maximo:float, unidad:str = "°C") -> None:
    # Bypass preventivo en el constructor para permitir temperaturas invernales negativas
    self._permitir_negativos:bool = True
    super().__init__(tag, valor_inicial, limite_maximo)
    self.unidad:str = unidad

  def verificar_alarma(self) -> bool:
    """
    Polimorfismo: Alarma por alta temperatura O por riesgo de congelamiento.
    """
    CONGELAMIENTO:float = 0.0
    return self.valor_actual > self.limite_maximo or self.valor_actual <= CONGELAMIENTO

# ------------------------------------------------------------------------------

# 1. Creación de instancias con diferentes escalas físicas
sensor_baja_presion = InstrumentoMedicion(tag="PT_MINI", valor_inicial=90.0, limite_maximo=100.0)   # 90% de saturación
sensor_alta_presion = InstrumentoMedicion(tag="PT_MAXI", valor_inicial=600.0, limite_maximo=1200.0) # 50% de saturación

# 2. Prueba de impresión (__str__ y __repr__)
print("--- Prueba de Representación ---")
print(sensor_baja_presion)  # Invoca __str__
print(f"Depuración: {sensor_baja_presion!r}\n")  # Invoca __repr__

# 3. Prueba de comparaciones gracias a @total_ordering
print("--- Prueba de Comparadores Matrimoniados ---")
print(f"¿Es PT_MINI más crítico que PT_MAXI?: {sensor_baja_presion > sensor_alta_presion}")  # Invoca __lt__ invertido -> True
print(f"¿Tienen el mismo tag?: {sensor_baja_presion == sensor_alta_presion}\n")              # Invoca __eq__ -> False

# 4. Ordenamiento Automático
print("--- Prueba de Ordenamiento de Lotes ---")
lote_sensores = [
  InstrumentoMedicion(tag="PT_01", valor_inicial=100.0, limite_maximo=1000.0), # 10%
  TransmisorPresion(tag="PT_02", valor_inicial=950.0, limite_maximo=1000.0), # 95%
  TransmisorTemperatura(tag="TT_01", valor_inicial=50.0, limite_maximo=100.0)  # 50%
]

# Python utiliza el método __lt__ internamente para ordenar la lista con .sort() o sorted()
sensores_ordenados = sorted(lote_sensores)

for s in sensores_ordenados:
  print(s)