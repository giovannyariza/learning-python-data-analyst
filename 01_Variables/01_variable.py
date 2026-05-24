# Una variable es un contenedor con un nombre identificador para almacenar un valor
# identificador = valor

# 1. Estilos de escritura de identificadores
id_cliente = 25 # snake_case, recomendada en Python
nombreCliente = 'Juan' # camelCase
CodigoProducto = "A45T24" # PascalCase o CapitalCamelCase
descripcionproducto = 'Monitor 27"' # flatcase

# ------------------------------------------------------------------------------

# 2. Python es sensible a mayúsculas en los identificadores
precio_unitario = 1529.75
Precio_Unitario = 879.65

print(precio_unitario) # 1529.75
print(Precio_Unitario) # 879.65

# ------------------------------------------------------------------------------

# 3. Tipado Dinámico (Duck Typing)
# Las variables en Python apuntan a un objeto, no están encasilladas en un tipo de dato
estacion_activa = 'Central' # Apunta inicialmente a una cadena

print(type(estacion_activa)) # class 'str'

estacion_activa = 5 # Ahora apunta a un Entero, totalmente válido en Python

print(type(estacion_activa)) # class 'int'

# ------------------------------------------------------------------------------

# 4. Asignación múltiple y elegante
# Asignar diferentes valores a diferentes variables en una sola línea
presion, temperatura, flujo = 145.7, 42.5, 1200.2

print(f"Presión: {presion}, Temperatura: {temperatura}, Flujo: {flujo}")

# Asignar el mismo valor a múltiples variables simultáneamente
limite_inferior = limite_superior = 0.0

# ------------------------------------------------------------------------------

# 5. Intercambio de valores (Swap)
# En otros lenguajes necesitas una variable 'auxiliar'. En Python es directo:
valor_a = 10
valor_b = 20
valor_a, valor_b = valor_b, valor_a  # Intercambio 'Pythonic'

print(f"A: {valor_a}, B: {valor_b}")

# ------------------------------------------------------------------------------

# 6. Constantes (Convención PEP 8)
# Se escriben en MAYÚSCULAS SOSTENIDAS para advertir a otros desarrolladores 
# que su valor NO debe ser modificado durante la ejecución.
PI = 3.14159
FACTOR_CONVERSION_BAR_PSI = 14.5038

# ------------------------------------------------------------------------------

# 7. Ayudas visuales en números grandes
# Puedes usar guiones bajos como separadores de miles para mejorar la legibilidad.
# Python los ignora al procesar el número.
total_registros_anuales = 12_500_000

print(total_registros_anuales)  # Imprime: 12500000