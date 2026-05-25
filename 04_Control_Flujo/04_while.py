# Ejemplo sencillo
contador = 0

while contador <= 10:
  print(f'Iteración: {contador}')
  contador += 1

# ------------------------------------------------------------------------------

def evaluar_paridad(numero:int) -> str:
  '''
  Evalua si un número dado es par o impar
  '''
  if numero % 2:
    return 'Impar'
  else:
    return 'Par'

# ------------------------------------------------------------------------------

def main() -> None:
  pregunta:str = 'Agrega un número y te diré si es par o impar.\r\n'
  pregunta += '(Escribe "cerrar" para salir de la aplicación)\r\n'
  continuar:bool = True

  while continuar:
    numero:str|int = input(pregunta)

    if numero == 'cerrar':
      continuar = False
    else:
      print(f'El número digitado es: {evaluar_paridad(int(numero))}.')

# ------------------------------------------------------------------------------

main()