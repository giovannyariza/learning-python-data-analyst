# `input()` siempre devuelve una cadena. La anotación `: str` indica el tipo esperado

# Se agrega un espacio al final de la cadena, por convención PEP 8
nombre:str = input('¿Cómo te llamas?\n')
# Si el usuario escribe texto no numérico, se lanzará `ValueError`
ano_nacimiento:int = int(input('¿En qué año naciste? '))
 # Cálculo aproximado de la edad. No considera mes/día de nacimiento
edad:int = 2026 - ano_nacimiento

print(f'Hola {nombre}, tienes aproximadamente {edad} años de edad.')

# Estructura condicional: evalúa si el usuario cumple la mayoría de edad legal
if edad >= 18:
  print('Ya tienes edad para votar!')
else:
  print('Aún no estas habilitado para votar.')

# ------------------------------------------------------------------------------

# Se solicita un número entero. El `\n` fuerza un salto de línea en la consola
numero = int(input('Agrega un número y te diré si es par o impar.\n'))

# El operador módulo (%) devuelve el residuo de la división entera
# En Python, cualquier número distinto de 0 se evalúa como `True` (truthy)
# Por eso `if numero % 2:` funciona: si el residuo es 1 (impar) → True
if numero % 2 != 0:
  print(f'El numero {numero} es impar')
else:
  print(f'El número {numero} es par')