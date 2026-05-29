# Una variable es un contenedor con un nombre identificador para almacenar un valor
# identificador = valor

# 1. Estilos de escritura de identificadores
well_id = 25 # snake_case, recomendada en Python
operatorName = 'Exxon' # camelCase
WellHeadCode = "A45-T24" # PascalCase o CapitalCamelCase
crudetype = 'Heavy crude oil' # flatcase

# ------------------------------------------------------------------------------

# 2. Python es sensible a mayúsculas en los identificadores
casing_pressure = 1529.75
Casing_Pressure = 879.65

print(casing_pressure) # 1529.75
print(Casing_Pressure) # 879.65

# ------------------------------------------------------------------------------

# 3. Tipado Dinámico (Duck Typing)
# Las variables en Python apuntan a un objeto, no están encasilladas en un tipo de dato
active_facility = 'CPF-01' # Apunta inicialmente a una cadena

print(type(active_facility)) # class 'str'

active_facility = 5 # Ahora apunta a un Entero, totalmente válido en Python

print(type(active_facility)) # class 'int'

# ------------------------------------------------------------------------------

# 4. Asignación múltiple y elegante
# Asignar diferentes valores a diferentes variables en una sola línea
pressure, temperature, flow_rate = 145.7, 42.5, 1200.2

print(f"Presión: {pressure}, Temperatura: {temperature}, Flujo: {flow_rate}")

# Asignar el mismo valor a múltiples variables simultáneamente
lower_alarm_limit = upper_alarm_limit = 0.0

# ------------------------------------------------------------------------------

# 5. Intercambio de valores (Swap)
# En otros lenguajes necesitas una variable 'auxiliar'. En Python es directo:
choke_a_flow = 450
choke_b_flow = 600

choke_a_flow, choke_b_flow = choke_b_flow, choke_a_flow  # Intercambio 'Pythonic'

print(f"A: {choke_a_flow}, B: {choke_b_flow}")

# ------------------------------------------------------------------------------

# 6. Constantes (Convención PEP 8)
# Se escriben en MAYÚSCULAS SOSTENIDAS para advertir a otros desarrolladores 
# que su valor NO debe ser modificado durante la ejecución.
BARREL_TO_GALLON_FACTOR = 42.0
STANDARD_ATMOSPHERIC_PRESSURE_PSI = 14.696

# ------------------------------------------------------------------------------

# 7. Ayudas visuales en números grandes
# Puedes usar guiones bajos como separadores de miles para mejorar la legibilidad.
# Python los ignora al procesar el número.
total_annual_barrel_production = 12_500_000

print(total_annual_barrel_production)  # Imprime: 12500000