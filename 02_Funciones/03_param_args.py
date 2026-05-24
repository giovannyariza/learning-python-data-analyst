# 1. Los parámetros son las variables de entrada que se declaran en la definición de la función
def identificacion(nombre:str):
  # print('Soy el gran ' + nombre)
  # print('Soy el gran', nombre)
  print(f'Soy el gran {nombre}')

identificacion('Gio')

# ------------------------------------------------------------------------------

# 2. Puede contener n cantidad de parámetros
def informacion(nombre:str, cargo:str) -> str:
  return f'Soy el gran {nombre} y soy {cargo}'

# Cuando se llama a la función los valores pasados a la función se le llaman argumentos
empleado_1:str = informacion('Gio', 'programador')
# empleado_2:str = informacion('Juan') # Genera error porque la función espera dos argumentos y son obligatorios

print(empleado_1)
# print(empleado_2) # ! Esto lanzará un TypeError

# ------------------------------------------------------------------------------

# 3. Parámetros por defecto
# Python permite definir valores predeterminados en los parámetros, haciendo que algunos argumentos
# sean opcionales al llamar la función.
def informacion_din(nombre:str, cargo:str = 'desconocido') -> str: # Parámetro por defecto (opcional)
  return f'Soy el gran {nombre} y soy {cargo}'

# Llamada sobreescribiendo el parámetro opcional
empleado_1:str = informacion_din('Gio', 'programador')
# Llamada omitiendo el parámetro opcional (toma el valor por defecto)
empleado_2:str = informacion_din('Juan') # Aquí no se genera error

print(empleado_1)
print(empleado_2)

# ------------------------------------------------------------------------------

# 4. Llamada mediante keywords (Argumentos por nombre)
# Python permite pasar argumentos en un orden diferente si especificas el nombre del parámetro
def calcular_imc(peso: float, altura: float) -> float:
  return peso / (altura ** 2)

# Pasar argumentos en orden estricto (Posicionales)
resultado_1:str = calcular_imc(96.7, 1.80)

print(resultado_1)

# Pasar argumentos en desorden pero explícitos (Keyword arguments)
# Es mucho más legible y evita errores de confusión de datos
resultado_2:str = calcular_imc(altura=1.80, peso=96.7)

print(f"IMC Calculado: {resultado_2:.2f}")