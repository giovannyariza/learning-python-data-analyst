nombre:str = input('¿Cómo te llamas?\r\n')
ano_nacimiento:int = int(input('¿En qué año naciste? '))
edad:int = 2026 - ano_nacimiento

print(f'Hola {nombre}, tienes aproximadamente {edad} años de edad.')

if edad >= 18:
  print('Ya tienes edad para votar!')
else:
  print('Aún no estas habilitado para votar.')

# ------------------------------------------------------------------------------

numero = int(input('Agrega un número y te diré si es par o impar.\r\n'))

if numero % 2:
  print(f'El numero {numero} es impar')
else:
  print(f'El número {numero} es par')