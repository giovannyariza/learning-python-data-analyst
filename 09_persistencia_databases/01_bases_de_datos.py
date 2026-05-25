import sqlite3

# 1. Definimos la Clase/Tabla (El espejo lógico)
class SensorTabla:
  __slots__ = ("tag", "lectura", "estado")

  def __init__(self, tag:str, lectura:float, estado:str = "OPERATIVO") -> None:
    self.tag:str = tag
    self.lectura:float = lectura
    self.estado:str = estado

  def guardar_en_base_datos(self, conexion:sqlite3.Connection) -> None:
    """
    Método ORM casero: Traduce las propiedades del objeto Python y las inserta
    de forma segura como una fila en la base de datos.
    """
    # El cursos es como el "bolígrafo" con el que escribimos en la base de datos
    cursor = conexion.cursor()

    # Orden segura de inserción. Los signos '?' son los contenedores seguros.
    consulta_sql = """
      INSERT INTO sensores (tag, lectura, estado)
      VALUES (?, ?, ?);
    """

    # Empaquetamos los datos del objeto en una tupla nativa
    datos_a_guardar:tuple[any] = (self.tag, self.lectura, self.estado)

    # El motor reemplaza los '?' por los datos de forma 100% segura
    cursor.execute(consulta_sql, datos_a_guardar)

    # Guardamos los cambios permanentemente en el archivo del disco duro
    conexion.commit()
    print(f"[Mini-ORM] Objeto '{self.tag}' guardado exitosamente en el archivo .db")

# ------------------------------------------------------------------------------

# 2. Configuración y Orquestación del Sistema
def inicializar_base_datos(conexion:sqlite3.Connection) -> None:
  """
  Crea la estructura de la tabla en la base de datos si no existe.
  """
  cursor = conexion.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensores (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      tag TEXT UNIQUE NOT NULL,
      lectura REAL NOT NULL,
      estado TEXT NOT NULL
    );
  """)

  conexion.commit()

# ------------------------------------------------------------------------------

def main() -> None:
  print('=== INICIANDO SISTEMA DE PERSISTENCIA ORM ===')

  # Abrimos la conexión al archivo de la base de datos usando Context Manager ('with')
  # Esto garantiza que el archivo se cierre correctamente si hay un apagón o un error
  with sqlite3.connect('./planta_industrial.db') as conexion_db:
    
    # Preparamos la base de datos creando la tabla
    inicializar_base_datos(conexion_db)

    # 3. Creamos tres objetos en nuestra oficina de Python (POO)
    print("\nInstanciando objetos en la memoria RAM...")
    sensor_alfa = SensorTabla(tag="PT_7214", lectura=1150.5)
    sensor_bravo = SensorTabla(tag="TT_3012", lectura=42.8)
    
    # 4. Le ordenamos a los objetos que se guarden a sí mismos en la base de datos
    # Intentamos guardarlos controlando errores si el 'tag' ya existe (Fase 4)
    try:
      sensor_alfa.guardar_en_base_datos(conexion_db)
      sensor_bravo.guardar_en_base_datos(conexion_db)
    except sqlite3.IntegrityError:
      print("[Advertencia] Los sensores ya existían en la base de datos. No se duplicaron.")

    # --- Verificación Analítica ---
    # Vamos a pedirle al traductor que nos muestre qué hay en la base de datos actual
    print("\nConsultando el Almacén Central (Base de Datos):")
    
    cursor = conexion_db.cursor()
    cursor.execute("SELECT * FROM sensores;")
    
    filas_tabla = cursor.fetchall()
    
    for fila in filas_tabla:
      print(f" -> Fila recuperada del disco duro: ID={fila[0]} | TAG='{fila[1]}' | Lectura={fila[2]} | Estado='{fila[3]}'")

  print("\n=== PROCESO FINALIZADO: Conexión cerrada de forma segura ===")

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()