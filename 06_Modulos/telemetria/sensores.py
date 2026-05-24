# Módulo de Definición de Estructuras de Datos

class InstrumentoMedicion:
  __slots__ = ('limite_maximo', 'tag', 'valor_actual')

  def __init__(self, tag:str, valor_inicial:float, limite_maximo:float) -> None:
    self.tag:str = tag
    self.limite_maximo:float = limite_maximo
    self.valor_actual:float = valor_inicial

    @property
    def valor_actual(self) -> float:
      return self._valor_actual
    
    @valor_actual.setter
    def valor_actual(self, nuevo_valor:float) -> None:
      if nuevo_valor < 0.0:
        raise ValueError(f'[{self.tag}] Error: No se permiten lecturas negativas.')
      self._valor_actual = nuevo_valor

# ------------------------------------------------------------------------------

# Guardían de pruebas unitarias
if __name__ == '__main__':
  print('=== [MODO PRUEBA] Ejecutando sensores.py directamente ===')
  sensor_test = InstrumentoMedicion('TEST_TAG', 50.0, 100.00)
  print(f'Objeto de prueba creado exitosamente: {sensor_test.tag}')