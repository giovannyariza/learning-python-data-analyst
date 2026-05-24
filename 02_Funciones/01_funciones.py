# Una función es un bloque de código reutilizable, diseñado para realizar una actividad

# 1. En Python, primero se debe definir la función y luego llamarla, de lo contrario dará error
# informacion() # ! Esto lanzará un NameError

# ------------------------------------------------------------------------------

# 2. Se define la función con la palabra reservada def
def informacion():
  # La indentación indica la pertenencia del código dentro de la función
  print('Soy el gran Gio')

print("Esto no forma parte de la función")

# ------------------------------------------------------------------------------

# 3. Llamada a la función
informacion()
# Se reutiliza cuantas veces se necesite
informacion()
informacion()