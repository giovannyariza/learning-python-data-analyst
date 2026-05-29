# =============================================================================
# OILFIELD ASSET CODE GENERATOR (Generador de Nomenclatura de Activos)
# =============================================================================
print("--------------------------------------------------")
print("Welcome to the Oilfield Asset Code Generator v1.0")
print("--------------------------------------------------")

# 1. ENTRADA DE DATOS (Captura de metadatos del campo)
# Solicitamos la cuenca geográfica (Geographic Basin)
basin_name:str = input("Enter the geographic basin name (e.g., Permian, Neuquina, Llanos):\n")

# Solicitamos las primeras 3 letras del tipo de fluido principal para crear un acrónimo
fluid_type:str = input("Enter the primary fluid type (e.g., Oil, Gas, Water):\n")

# Solicitamos el número de pozo o plataforma (debe ser entero para validar la telemetría)
well_number:int = int(input("Enter the well or platform sequential number: "))

# 2. PROCESAMIENTO Y LIMPIEZA DE DATOS (Simulación de estandarización)
# Extraemos los primeros 3 caracteres en MAYÚSCULAS para estandarizar el código
basin_code:str = basin_name[:3].upper()
fluid_code:str = fluid_type[:3].upper()

# 3. GENERACIÓN DEL CÓDIGO FINAL (Uso de f-strings con formateo de números)
# Usamos ':03d' para que el número siempre tenga 3 dígitos (ej: el pozo 5 se convierte en 005)
asset_tag:str = f"{basin_code}-{fluid_code}-{well_number:03d}"

# 4. SALIDA DE DATOS
print("\n--------------------------------------------------")
print(f"Asset Configuration Successful!")
print(f"The official SCADA tag for your new well is: {asset_tag}")
print("--------------------------------------------------")