class InstrumentoMedicion:
  # Convención privada: (_atributo) indica atributo para acceso interno de la clase
  __slots__ = ('tag', '_valor_actual', 'limite_maximo')


  def __init__(self, tag:str, valor_inicial:float, limite_maximo:float) -> None:
    """
    Inicializa un nuevo instrumento de medición con sus umbrales operativos.
    """
    self.tag:str = tag
    self.limite_maximo:float = limite_maximo
    # Usamos el setter directamente desde la inicialización para validar el dato de entrada
    self.valor_actual:float = valor_inicial

  # Decorador que expone un método con el nombre limpio, que se comporta externamente 
  # como un atributo normal de lectura
  @property
  def valor_actual(self) -> float:
    """
    Getter: Expone el valor actual de la medición como si fuera un atributo público.
    """
    return self._valor_actual

  # Intercepta cualquier intento de escribir datos en la propiedad.
  @valor_actual.setter
  def valor_actual(self, nuevo_valor: float) -> None:
    """
    Setter: Intercepta la asignación, valida la coherencia física del dato
    y actualiza el estado interno o lanza una excepción.
    """
    if nuevo_valor < 0.0:
      raise ValueError(
        f"[{self.tag}] Error Crítico: No se permiten lecturas negativas ({nuevo_valor})."
      )
    self._valor_actual = nuevo_valor


  def verificar_alarma(self) -> bool:
    """
    Evalúa si la lectura actual supera el límite máximo de seguridad.
    """
    return self._valor_actual > self.limite_maximo

# ------------------------------------------------------------------------------

# 1. Instanciación correcta
sensor_presion = InstrumentoMedicion(tag="PT_7214", valor_inicial=1150.0, limite_maximo=1200.0)
sensor_temperatura = InstrumentoMedicion(tag="TT_3012", valor_inicial=45.2, limite_maximo=85.0)

print(f"Estado inicial {sensor_temperatura.tag}: {sensor_temperatura.valor_actual} °F")

# 2. Lectura y modificación limpia (Se ejecuta el Getter y el Setter detrás de escena)
sensor_temperatura.valor_actual = 92.3

print(f'Nueva lectura de temperatura: {sensor_temperatura.valor_actual} °F')

print(f"¿Alarma en {sensor_presion.tag}?: {sensor_presion.verificar_alarma()}") # Salida: True
print(f"¿Alarma en {sensor_temperatura.tag}?: {sensor_temperatura.verificar_alarma()}") # Salida: False

# 3. Intento de corrupción de datos envuelto en un bloque de control de excepciones (Fase 4)
try:
  print("\nIntentando inyectar una lectura corrupta (-15.0)...")
  sensor_temperatura.valor_actual = -15.0  # Esto disparará el ValueError dentro del setter
except ValueError as error:
  print(f"Manejador de Excepciones activado exitosamente -> {error}")

# El objeto permanece a salvo en su último estado válido conocida
print(f"Estado final seguro del objeto: {sensor_temperatura.valor_actual} °F")