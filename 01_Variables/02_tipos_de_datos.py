# 1. Tipos de datos y Type Hints (Pistas de Tipo)
# Type Hint: Es una sintaxis formal para declarar el tipo de dato esperado en 
# las variables, parámetros de funciones y valores de retorno. Puramente informativo.

# Strings o Cadenas de Texto
nombre:str = 'Giovanny' # Entre comillas simples
profesion:str = "Analista de Datos" # Entre comillas dobles

print(nombre)
print(profesion)

# Integers o números enteros (sin decimales)
edad:int = 47

print(edad)

# Floats o números flotantes (con punto decimal)
peso:float = 96.7

print(peso)

# Booleanos (Verdadero o Falso)
es_mayor_de_edad:bool = True

print(es_mayor_de_edad)

# ------------------------------------------------------------------------------

# 2. Conversión de tipos (Casting)
# Es crucial cuando procesas datos externos (vienen como texto y necesitas operar)
edad_texto: str = "47"
# edad_calculada = edad_texto + 1 # !! Esto lanzará un TypeError

edad_numerica: int = int(edad_texto) # Conversión explícita a entero

print(edad_numerica + 1) # Ahora es seguro operar (Imprime 48)

# Conversión implícita (Python promueve el tipo automáticamente para no perder precisión)
resultado_operacion: float = 10 + 4.5 # int + float = float

print(type(resultado_operacion)) # <class 'float'>

# ------------------------------------------------------------------------------

# 3. Interpolación avanzada y formateo (f-strings)
# Las f-strings permiten incrustar expresiones y formatear la salida visualmente
nombre: str = "Giovanny"
profesion: str = "Analista de Datos"
peso: float = 96.7456

# Formatear texto plano combinando variables
print(f"Empleado: {nombre} | Rol: {profesion}")

# Control de precisión en flotantes (: .2f limita a 2 decimales y redondea)
print(f"El peso registrado es de {peso:.2f} kg.") 

# ------------------------------------------------------------------------------

# 4. Comportamiento de booleanos (Truthy y Falsy)
# En Python, otros tipos de datos pueden evaluar como True o False en estructuras de control
# Valores "Falsy" comunes: 0, "", [], {}, None. Cualquier otro valor suele ser "Truthy"
nombre_usuario: str = "" # String vacío
evaluacion_booleana: bool = bool(nombre_usuario)

print(f"¿El string vacío es verdadero?: {evaluacion_booleana}")  # Imprime False

# ------------------------------------------------------------------------------

# 5. El tipo especial: NoneType (Ausencia de valor)
# Representa datos faltantes o nulos (es el equivalente al 'NaN' en Pandas o 'NULL' en SQL)
registro_sensor: None = None

print(type(registro_sensor))  # <class 'NoneType'>