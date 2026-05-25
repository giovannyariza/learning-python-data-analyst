def simple_while() -> None:
  # Ejemplo sencillo
  contador = 0

  while contador <= 10:
    print(f'Iteración: {contador}')
    contador += 1

# ------------------------------------------------------------------------------

# simple_while()

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

# main()

# ------------------------------------------------------------------------------

playlist = {} # Diccionario vacío
playlist['canciones'] = [] # Lista vacía en el diccionario


def mostrar_resumen() -> None:
  print(f'Playlist: {playlist["nombre"]}\r\n')
  print('Canciones:')

  for cancion in playlist['canciones']:
    print(cancion)

# ------------------------------------------------------------------------------

def agregar_canciones() -> None:
  agregar_cancion:bool = True

  while agregar_cancion:
    nombre_playlist:str = playlist['nombre']
    pregunta:str = f'\r\nAgrega canciones para la playlist {nombre_playlist}:\r\n'
    pregunta += 'Escribe "x" para dejar de agregar canciones.\r\n'

    cancion:str = input(pregunta)

    if cancion == 'x':
      agregar_cancion = False
      mostrar_resumen()
    else:
      playlist['canciones'].append(cancion)

# ------------------------------------------------------------------------------

def app():
  agregar_playlist:bool = True

  while agregar_playlist:
    nombre_playlist:str = input('¿Cómo deseas nombrar la playlist? ')

    if nombre_playlist:
      playlist['nombre'] = nombre_playlist
      agregar_playlist = False

      agregar_canciones()

# ------------------------------------------------------------------------------

app()