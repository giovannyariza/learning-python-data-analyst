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


  def verificar_alarma(self) -> bool:
    return self._valor_actual > self.limite_maximo

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

# Creamos una lista heterogénea de objetos bajo el tipo general del padre
sistema_telemetria: list[InstrumentoMedicion] = [
  TransmisorPresion(tag="PT_7214", valor_inicial=1180.0, limite_maximo=1200.0),
  TransmisorPresion(tag="PT_7215", valor_inicial=1250.0, limite_maximo=1200.0),
  TransmisorTemperatura(tag="TT_3012", valor_inicial=25.4, limite_maximo=85.0),
  TransmisorTemperatura(tag="TT_3013", valor_inicial=-5.2, limite_maximo=85.0)  # Disparará por congelamiento
]

print("=== MONITOREO DE SISTEMAS CENTRALIZADO ===")
# Tratamiento polimórfico: A Python no le interesa la subclase exacta, solo que implemente la interfaz
for instrumento in sistema_telemetria:
  tag:str = instrumento.tag
  lectura:float = instrumento.valor_actual
  
  # Cada objeto ejecuta SU propia versión de verificar_alarma()
  estado_alarma:str = "¡ALERTA DISPARADA!" if instrumento.verificar_alarma() else "NORMAL OK"
  
  print(f"Instrumento: {tag} | Lectura: {lectura} | Estado: {estado_alarma}")