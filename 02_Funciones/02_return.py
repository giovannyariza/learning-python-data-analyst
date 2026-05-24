# Funciones que retornan un valor para que otra parte del código pueda guardarlo en una variable
# y seguir trabajando con él.

# 1. Función con parámetros y retorno
# Recibe dos parámetros (str e int) y devuelve un string (-> str)
def identificacion(nombre:str) -> str:
  return f'Hola, soy {nombre}'

# Llamada a la función y captura del valor
# Guardamos lo que retorna la función dentro de una nueva variable
saludo_final:str = identificacion('Giovanny')

print(saludo_final)