# 1. Tipos de datos y Type Hints (Pistas de Tipo)
# Type Hint: Es una sintaxis formal para declarar el tipo de dato esperado en 
# las variables, parámetros de funciones y valores de retorno. Puramente informativo.

# Strings o Cadenas de Texto
well_name:str = 'CA-105' # Entre comillas simples
fluid_type:str = "Diluted Crude Oil" # Entre comillas dobles

print(well_name)
print(fluid_type)

# Integers o números enteros (sin decimales)
active_valves:int = 14

print(active_valves)

# Floats o números flotantes (con punto decimal)
api_gravity:float = 13.5 # Gravedad API

print(api_gravity)

# Booleanos (Verdadero o Falso)
esd_active:bool = True # Emergency Shut Down (Parada de Emergencia)

print(esd_active)

# ------------------------------------------------------------------------------

# 2. Conversión de tipos (Casting)
# Es crucial cuando procesas datos externos (vienen como texto y necesitas operar)
pressure_raw_text:str = "2450"
# total_pressure = pressure_raw_text + 50 # !! Esto lanzará un TypeError

pressure_psi:int = int(pressure_raw_text) # Conversión explícita a entero

print(pressure_psi + 50) # Ahora es seguro operar (Imprime 2500)

# Conversión implícita (Python promueve el tipo automáticamente para no perder precisión)
final_density:float = 850 + 0.45 # int + float = float

print(type(final_density)) # <class 'float'>

# ------------------------------------------------------------------------------

# 3. Interpolación avanzada y formateo (f-strings)
# Las f-strings permiten incrustar expresiones y formatear la salida visualmente
well_name:str = "CAN-232"
fluid_type:str = "Heavy Crude"
flow_rate_bpd:float = 430.9689

# Formatear texto plano combinando variables
print(f"Asset: {well_name} | Fluid Category: {fluid_type}")

# Control de precisión en flotantes (: .2f limita a 2 decimales y redondea)
print(f"Current production rate is {flow_rate_bpd:.2f} BPD.") 

# ------------------------------------------------------------------------------

# 4. Comportamiento de booleanos (Truthy y Falsy)
# En Python, otros tipos de datos pueden evaluar como True o False en estructuras de control
# Valores "Falsy" comunes: 0, "", [], {}, None. Cualquier otro valor suele ser "Truthy"
diagnostic_log:str = "" # String vacío
has_errors:bool = bool(diagnostic_log)

print(f"¿The log registered activity?: {has_errors}")  # Imprime False

# ------------------------------------------------------------------------------

# 5. El tipo especial: NoneType (Ausencia de valor)
# Representa datos faltantes o nulos (es el equivalente al 'NaN' en Pandas o 'NULL' en SQL)
bottomhole_sensor:None = None

print(type(bottomhole_sensor))  # <class 'NoneType'>